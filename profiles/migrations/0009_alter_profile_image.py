# Generated by Django 3.2.5 on 2021-07-28 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/img/menprofile_mirh47.png', upload_to='', verbose_name='image'),
        ),
    ]
