from datetime import datetime

from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    gender = models.CharField(max_length=2, null=True, choices=(("M", "男"), ("F", "女")), help_text="性别")
    mobile = models.CharField(max_length=12, null=False, verbose_name=u"电话", unique=True, help_text="电话")
    address = models.CharField(max_length=50, verbose_name=u"地址", help_text="地址")
    email = models.EmailField(verbose_name=u"邮箱", null=True, help_text="邮箱")
    image = models.ImageField(upload_to="image/user/%Y/%m", verbose_name=u"头像", help_text="头像")
    wallet = models.FloatField(default=100, verbose_name=u"钱包", null=False, help_text="钱包")
    add_time = models.DateField(default=timezone.now, verbose_name=u"添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = "user"

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码", help_text="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话", help_text="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name
        db_table = "mobile_code"

    def __str__(self):
        return "mobile:" + self.mobile + "；code:" + self.code


class Base(models.Model):
    # 基地
    name = models.CharField(max_length=50, verbose_name=u"基地名称", null=False, help_text="基地名称")
    address = models.CharField(max_length=50, verbose_name=u"基地地址", null=False, help_text="基地地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "基地信息"
        verbose_name_plural = verbose_name
        db_table = "base"

    def __str__(self):
        return self.name


class Staff(models.Model):
    # 员工
    name = models.CharField(max_length=50, verbose_name=u"员工姓名", null=False, help_text="员工姓名")
    mobile = models.CharField(max_length=12, verbose_name=u"员工电话", null=False, help_text="员工电话")
    salary = models.FloatField(max_length=20, default=0, verbose_name=u"工资", help_text="员工工资")
    seniority = models.IntegerField(verbose_name=u"工龄", null=True, help_text="工龄")
    base = models.ForeignKey(Base, verbose_name=u"基地地址", on_delete=models.CASCADE, help_text="所属基地")
    add_time = models.DateField(default=timezone.now, verbose_name=u"添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = verbose_name
        db_table = "staff"

    def __str__(self):
        return self.name


class News(models.Model):
    image = models.ImageField(upload_to="image/news/%Y/%m", verbose_name=u"新闻图片", help_text="新闻图片")
    title = models.CharField(max_length=1024, verbose_name=u"新闻标题", null=False, help_text="新闻标题")
    content = models.CharField(max_length=2048, verbose_name=u"新闻内容", null=False, help_text="新闻内容")
    author = models.CharField(max_length=20, verbose_name=u"新闻作者", null=False, help_text="新闻作者")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "新闻信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + " written By " + self.author


class Banner(models.Model):
    index = models.AutoField(primary_key=True, verbose_name=u"顺序", help_text="轮播图顺序")
    content = models.ForeignKey(News, verbose_name=u"新闻标题", on_delete=models.CASCADE, help_text="内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间", help_text="添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
        db_table = "banner"

    def __str__(self):
        return "轮播内容:" + self.content.__str__()
