# Generated by Django 3.0 on 2020-10-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0056_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
