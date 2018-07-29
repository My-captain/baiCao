from django.db import models
from users.models import Base

from datetime import datetime
from django.utils import timezone

# Create your models here.


class Goods(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"商品名称", null=False)
    type = models.CharField(max_length=10, verbose_name=u"商品类型", null=False,
                            choices=(("seed", "种子"), ("pot", "花盆"), ("soil", "营养土"), ("muck", "肥料")), default="seed")
    price = models.FloatField(verbose_name=u"商品价格", null=False)
    count = models.IntegerField(verbose_name=u"商品数量", null=False)
    base = models.ForeignKey(Base, null=True, verbose_name=u"所属基地", on_delete=models.CASCADE)
    desc = models.CharField(max_length=200, verbose_name=u"商品简介")
    img = models.ImageField(upload_to="image/goods/%Y/%m", verbose_name=u"商品图片")
    add_time = models.DateField(default=timezone.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name
        db_table = "goods"

    def __str__(self):
        return self.name


class Plants(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"植物名称", null=False)
    classes = models.CharField(max_length=50, verbose_name=u"门纲科目", null=False)
    specification = models.CharField(max_length=50, verbose_name=u"规格", null=False)
    flowering = models.CharField(max_length=50, verbose_name=u"花期", null=False)
    medicinal_parts = models.CharField(max_length=50, verbose_name=u"药用部位", null=False)
    flavour = models.CharField(max_length=50, verbose_name=u"性味", null=False)
    function = models.CharField(max_length=50, verbose_name=u"功能", null=False)
    image = models.ImageField(upload_to="image/plants/%Y/%m", verbose_name=u"植物图片")
    add_time = models.DateField(default=timezone.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "植物信息"
        verbose_name_plural = verbose_name
        db_table = "plants"

    def __str__(self):
        return self.name
