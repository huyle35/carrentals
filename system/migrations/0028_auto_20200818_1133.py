# Generated by Django 3.0 on 2020-08-18 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0027_auto_20200818_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tên_khách_hàng',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='số_điện_thoại',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='tên_khách_hàng',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='system.Customer'),
        ),
    ]
