# Generated by Django 3.0.3 on 2020-02-23 00:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_profileadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='picture'),
        ),
    ]
