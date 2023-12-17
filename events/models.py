from django.db import models
import base64
from PIL import Image
from io import BytesIO


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    image_base64 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# class UserLogIn(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.email
