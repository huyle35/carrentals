# Generated by Django 2.2.13 on 2020-08-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0043_auto_20200823_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ngày_về',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='ngày_đi',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='quote',
            name='ngày_về',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='quote',
            name='ngày_đi',
            field=models.DateField(),
        ),
    ]
