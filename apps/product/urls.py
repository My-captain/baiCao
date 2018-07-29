from django.urls import re_path
from django.conf.urls import url, include

from .views import GoodsView, PlantsView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'goods', GoodsView)
router.register(r'plants', PlantsView)

urlpatterns = [
    url(r'^', include(router.urls)),
]

app_name = 'product'
