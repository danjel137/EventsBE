# Generated by Django 4.2.7 on 2023-11-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_base64',
            field=models.TextField(blank=True, null=True),
        ),
    ]
