# Generated by Django 4.2.7 on 2023-11-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_photo_image_base64'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
