# Generated by Django 3.2.5 on 2021-07-28 23:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20210729_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='static/img/menprofile_mirh47.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]