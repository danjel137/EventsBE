# Generated by Django 4.2.7 on 2023-11-29 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_photo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
    ]
