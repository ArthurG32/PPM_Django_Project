# Generated by Django 4.2.1 on 2023-06-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_PPM', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo/'),
        ),
    ]
