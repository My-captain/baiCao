# ==========================================
# @Time    : 2018/7/28 14:59
# @Author  : Mr.Robot
# @File    : filters.py
# @Project : baiCao
# ==========================================

import django_filters
from .models import Goods, Plants


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    GoodsFilter
    """
    name = django_filters.CharFilter(lookup_expr="icontains", label="根据商品名搜索")
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="price_gt", label="价格区间搜索(greater than)")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="price_lt", label="价格区间搜索(less than)")

    class Meta:
        model = Goods
        fields = ["name", "type", "price"]


class PlantsFilter(django_filters.rest_framework.FilterSet):
    """
    PlantsFilter
    """
    name = django_filters.CharFilter(lookup_expr="icontains")
    medicinal_parts = django_filters.CharFilter(lookup_expr="icontains")
    classes = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Plants
        fields = ["name", "classes", "medicinal_parts", "flavour", "function"]
