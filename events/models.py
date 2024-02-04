from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image_base64 = models.TextField(blank=True, null=True)
    date_created = models.DateField(default=timezone.now().date())

    def __str__(self):
        return self.title


# class UserLogIn(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.email

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    birthday = models.DateField(default="2000-01-01")


def __str__(self):
    return self.user.username
