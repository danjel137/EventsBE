from django.db import models
import base64
from PIL import Image
from io import BytesIO


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    image_base64 = models.TextField(blank=True, null=True)


    # def save(self, *args, **kwargs):
    #     if self.image:
    #         # Open the image using PIL
    #         img = Image.open(self.image)
    #         img_io = BytesIO()
    #
    #         # Convert the image to base64 string
    #         img.save(img_io, format='PNG')
    #         img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    #         self.image_base64 = img_base64
    #
    #     super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
