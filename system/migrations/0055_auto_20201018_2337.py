# Generated by Django 3.0 on 2020-10-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0054_auto_20201018_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='variables',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]