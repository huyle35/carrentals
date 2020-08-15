# Generated by Django 3.0 on 2020-08-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0016_auto_20200815_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='giá',
        ),
        migrations.AddField(
            model_name='car',
            name='giá_tham_khảo',
            field=models.FloatField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='số_điện_thoại',
            field=models.IntegerField(),
        ),
    ]
