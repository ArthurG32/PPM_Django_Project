# Generated by Django 4.2.1 on 2023-05-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_PPM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
