from rest_framework import mixins
from rest_framework import viewsets

# 自定义分页器
from utils.Pagination import Pagination

from .serializers import GoodsSerializer, PlantsSerializer
from .models import Goods, Plants

# 过滤器
from django_filters import rest_framework as filters
from .filters import GoodsFilter, PlantsFilter

# Create your views here.


class GoodsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品
    """
    pagination_class = Pagination
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = GoodsFilter
    ordering_fields = ('price', 'count', 'add_time')


class PlantsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    植物
    """
    pagination_class = Pagination
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = PlantsFilter
    ordering_fields = ('add_time', )
