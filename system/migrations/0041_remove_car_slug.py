# Generated by Django 2.2.13 on 2020-08-22 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0040_car_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='slug',
        ),
    ]