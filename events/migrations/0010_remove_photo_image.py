# Generated by Django 4.2.7 on 2023-12-01 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_photo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
    ]