# Generated by Django 4.2.7 on 2024-02-04 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_photo_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date_created',
            field=models.DateField(default=datetime.date(2024, 2, 4)),
        ),
    ]