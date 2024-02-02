from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Photo, Account


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "password"]
#
#     def create(self, validated_data):
#         user = User.objects.create(username=validated_data["username"])
#         user.set_password(validated_data["password"])
#         user.save()
#         return user
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['gender', 'birthday']


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'account']

    def create(self, validated_data):
        account_data = validated_data.pop('account', {})
        user = User.objects.create(username=validated_data['username'])
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
