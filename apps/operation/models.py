from django.db import models
from datetime import datetime

from users.models import UserProfile, Staff
from product.models import Goods
# Create your models here.


class Generation(models.Model):
    customer = models.ForeignKey(UserProfile, verbose_name=u"顾客", on_delete=models.CASCADE, help_text="顾客id")
    staff = models.ForeignKey(Staff, verbose_name=u"代种员工", on_delete=models.CASCADE, help_text="员工id")
    begin = models.DateField(verbose_name=u"开始时间", null=False, help_text="开始时间")
    end = models.DateField(verbose_name=u"结束时间", null=False, help_text="结束时间")
    deliver_type = models.CharField(
        max_length=10, verbose_name=u"快递方式",
        choices=(
            ("client", "客户负责"),
            ("server", "服务员上门")),
        default="client"
        , help_text="快递方式")
    plant_type = models.CharField(
        max_length=10, verbose_name=u"盆栽类型",
        choices=(
            ("small", "小型"),
            ("middle", "中型"),
            ("large", "大型")
        ),
        default="small"
        , help_text="盆栽类型")
    address = models.CharField(max_length=50, verbose_name=u"地址", null=False, help_text="地址")
    price = models.FloatField(max_length=20, verbose_name=u"代种价格", null=False, help_text="价格")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "代种信息"
        verbose_name_plural = verbose_name
        db_table = "generation"

    def __str__(self):
        return self.customer.username + "种植" + self.plant_type


class Purchase(models.Model):
    customer = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE, help_text="用户id")
    goods = models.ForeignKey(Goods, verbose_name=u"商品", on_delete=models.CASCADE, help_text="商品id")
    count = models.IntegerField(verbose_name=u"数量", null=False, help_text="数量")
    total_money = models.FloatField(max_length=100, verbose_name=u"金额", null=False, help_text="总金额")
    state = models.IntegerField(
        verbose_name=u"购买状态",
        choices=(
            (1, "已支付"),
            (2, "已发货"),
            (3, "运输中"),
            (4, "已到站"),
            (5, "已提货")
        ), default=1, help_text="货物状态")
    address = models.CharField(max_length=50, verbose_name=u"收货地址", null=False, help_text="地址")
    mobile = models.CharField(max_length=11, verbose_name=u"联系电话", null=False, help_text="电话")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name = "购买信息"
        verbose_name_plural = verbose_name
        db_table = "purchase"

    def __str__(self):
        return self.customer.username + str(self.count) + "件" + self.goods.name


class Favorite(models.Model):
    customer = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE, help_text="用户id")
    good = models.ForeignKey(Goods, verbose_name=u"商品", on_delete=models.CASCADE, help_text="商品id")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        unique_together = ('customer', 'good')
        verbose_name = "收藏信息"
        verbose_name_plural = verbose_name
        db_table = "favorite"

    def __str__(self):
        return self.customer.username + "*" + self.good.name

