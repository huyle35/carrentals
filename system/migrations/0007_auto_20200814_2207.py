# Generated by Django 3.0 on 2020-08-14 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20200814_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='cost_par_day',
            new_name='giá',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='image',
            new_name='hình_ảnh',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='height_field',
            new_name='lượt_thích',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='content',
            new_name='nội_dung',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='num_of_seats',
            new_name='số_ghế',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='company_name',
            new_name='tên_công_ty',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='số_điện_thoại',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='tên',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='name',
            new_name='tên_khách_hàng',
        ),
        migrations.RenameField(
            model_name='privatemsg',
            old_name='message',
            new_name='nội_dung',
        ),
        migrations.RenameField(
            model_name='privatemsg',
            old_name='name',
            new_name='tên_người_dùng',
        ),
        migrations.RemoveField(
            model_name='car',
            name='like',
        ),
        migrations.RemoveField(
            model_name='car',
            name='width_field',
        ),
        migrations.RemoveField(
            model_name='history',
            name='day',
        ),
    ]
