# Generated by Django 4.2.7 on 2024-02-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_remove_photo_created_at_remove_photo_owner_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='owner_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
