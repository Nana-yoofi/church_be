# Generated by Django 4.0.8 on 2023-01-25 20:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0006_alter_videopodcast_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopodcast',
            name='url',
            field=cloudinary.models.CloudinaryField(default="url",max_length=255),
        ),
    ]
