# Generated by Django 3.0 on 2020-10-21 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0056_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
