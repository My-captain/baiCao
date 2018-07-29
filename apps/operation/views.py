# ==========================================
# @Time    : 2018/7/29 9:42
# @Author  : Mr.Robot
# @File    : views.py
# @Project : baiCao
# ==========================================

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import Purchase, Favorite, Generation
from .serializers import PurchaseSerializer, FavoriteSerializer, GenerationSerializer

# 自定义权限认证
from utils import permissions

# Create your views here.


class PurchaseViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户购买接口
    """
    queryset = Purchase.objects.all()
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = PurchaseSerializer

    # 该方法只能获取到当前用户的购买记录
    def get_queryset(self):
        return Purchase.objects.filter(customer=self.request.user)


class GenerationView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户代种接口
    """
    queryset = Generation.objects.all()
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GenerationSerializer

    # 该方法只能获取到当前用户的购买记录
    def get_queryset(self):
        return Generation.objects.filter(customer=self.request.user)


class FavoriteView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户收藏接口
    """
    queryset = Favorite.objects.all()
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = FavoriteSerializer

    # 该方法只能获取到当前用户的购买记录
    def get_queryset(self):
        return Favorite.objects.filter(customer=self.request.user)


