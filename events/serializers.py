from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Photo, Account
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['gender', 'birthday']


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(write_only=True)
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password_confirmation', 'account']

    def generate_unique_username(self, first_name, last_name):
        base_username = f"{first_name.lower()}.{last_name.lower()}"
        username = base_username
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{base_username}.{counter}"
            counter += 1

        return username

    def compare_passwords(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.get('password_confirmation')

        # Check if passwords match
        return password == password_confirmation

    def create(self, validated_data):
        account_data = validated_data.pop('account', {})

        # Check if passwords match
        if not self.compare_passwords(validated_data):
            raise serializers.ValidationError({"password": "Passwords do not match"})

        # Generate a unique username by concatenating first name and last name
        username = self.generate_unique_username(validated_data['first_name'], validated_data['last_name'])

        user = User.objects.create(
            username=username,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        Account.objects.create(user=user, **account_data)

        return user


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

# class UserLogInSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserLogIn
#         fields = '__all__'


# {
#     "first_name":"Danjel",
#     "last_name":"Halili",
#     "email":"danjelhalili2@gmail.com",
#     "password": "password123",
#     "password_confirmation": "password123",
#     "account": {
#         "gender": "male",
#         "birthday": "1990-01-01"
#     }
# }
