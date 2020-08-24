# Generated by Django 3.0 on 2020-08-15 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20200815_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('số_điện_thoại', models.CharField(max_length=15)),
                ('ngày_đi', models.DateTimeField()),
                ('ngày_về', models.DateTimeField()),
                ('xuất_phát', models.CharField(max_length=100)),
                ('điểm_đến', models.CharField(max_length=100)),
                ('tên_xe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote', to='system.Car')),
            ],
        ),
    ]