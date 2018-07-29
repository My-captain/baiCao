# Generated by Django 2.0.1 on 2018-07-28 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名称')),
                ('type', models.CharField(choices=[('seed', '种子'), ('pot', '花盆'), ('soil', '营养土'), ('muck', '肥料')], default='seed', max_length=10, verbose_name='商品类型')),
                ('price', models.FloatField(verbose_name='商品价格')),
                ('count', models.IntegerField(verbose_name='商品数量')),
                ('desc', models.CharField(max_length=200, verbose_name='商品简介')),
                ('img', models.ImageField(upload_to='image/goods/%Y/%m', verbose_name='商品图片')),
                ('add_time', models.DateField(default=datetime.datetime(2018, 7, 28, 11, 19, 2, 158303), verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '商品信息',
                'verbose_name': '商品信息',
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='植物名称')),
                ('classes', models.CharField(max_length=50, verbose_name='门纲科目')),
                ('specification', models.CharField(max_length=50, verbose_name='规格')),
                ('phase', models.CharField(max_length=50, verbose_name='花期')),
                ('parts', models.CharField(max_length=50, verbose_name='药用部位')),
                ('flavour', models.CharField(max_length=50, verbose_name='性味')),
                ('function', models.CharField(max_length=50, verbose_name='功能')),
                ('image', models.ImageField(upload_to='image/plants/%Y/%m', verbose_name='植物图片')),
                ('add_time', models.DateField(default=datetime.datetime(2018, 7, 28, 11, 19, 2, 159286), verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '植物信息',
                'verbose_name': '植物信息',
                'db_table': 'plants',
            },
        ),
    ]