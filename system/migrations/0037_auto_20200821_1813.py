# Generated by Django 2.2.13 on 2020-08-21 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0036_auto_20200821_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='category',
            new_name='danh_mục',
        ),
    ]