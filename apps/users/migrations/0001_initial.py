# Generated by Django 2.0.1 on 2018-07-28 11:19

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=2, null=True)),
                ('mobile', models.CharField(max_length=12, unique=True, verbose_name='电话')),
                ('address', models.CharField(max_length=50, verbose_name='地址')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('image', models.ImageField(upload_to='image/user/%Y/%m', verbose_name='头像')),
                ('wallet', models.FloatField(default=100, verbose_name='钱包')),
                ('add_time', models.DateField(default=datetime.datetime(2018, 7, 28, 11, 19, 2, 154306), verbose_name='添加时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户信息',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False, verbose_name='顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='基地名称')),
                ('address', models.CharField(max_length=50, verbose_name='基地地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '基地信息',
                'verbose_name': '基地信息',
                'db_table': 'base',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/news/%Y/%m', verbose_name='新闻图片')),
                ('title', models.CharField(max_length=1024, verbose_name='新闻标题')),
                ('content', models.CharField(max_length=2048, verbose_name='新闻内容')),
                ('author', models.CharField(max_length=20, verbose_name='新闻作者')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '新闻信息',
                'verbose_name': '新闻信息',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='员工姓名')),
                ('mobile', models.CharField(max_length=12, verbose_name='员工电话')),
                ('salary', models.FloatField(default=0, max_length=20, verbose_name='工资')),
                ('seniority', models.IntegerField(null=True, verbose_name='工龄')),
                ('add_time', models.DateField(default=datetime.datetime(2018, 7, 28, 11, 19, 2, 156304), verbose_name='添加时间')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Base', verbose_name='基地地址')),
            ],
            options={
                'verbose_name_plural': '员工信息',
                'verbose_name': '员工信息',
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='验证码')),
                ('mobile', models.CharField(max_length=11, verbose_name='电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '短信验证码',
                'verbose_name': '短信验证码',
                'db_table': 'mobile_code',
            },
        ),
        migrations.AddField(
            model_name='banner',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.News', verbose_name='新闻标题'),
        ),
    ]
