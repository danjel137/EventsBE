# Generated by Django 4.2.7 on 2023-11-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_photo_description_alter_photo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
