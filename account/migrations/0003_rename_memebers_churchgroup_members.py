# Generated by Django 4.0.8 on 2023-01-21 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_churchgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='churchgroup',
            old_name='memebers',
            new_name='members',
        ),
    ]
