# Generated by Django 2.0.1 on 2018-07-23 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_goods_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2018, 7, 23, 11, 41, 18, 80633), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='plants',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2018, 7, 23, 11, 41, 18, 81632), verbose_name='添加时间'),
        ),
    ]
