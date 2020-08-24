# Generated by Django 3.0 on 2020-08-15 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0010_auto_20200815_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tên_khách_hàng',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tên_xe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_ten_xe', to='system.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]