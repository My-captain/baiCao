from django.urls import path, re_path
from product import views


urlpatterns = [
    re_path(r'goods/list/$', views.GoodsListView.as_view(), name="goods_list"),
    re_path(r'plants/list/$', views.PlantsListView.as_view(), name="plants_list"),

    re_path(r'plants/search/$', views.PlantsSearchView.as_view(), name="plants_search"),

    # 植物分类
    re_path(r'plants/category/(?P<type>\d)/$', views.PlantsCategoryView, name="plants_category"),

    # 商品分类
    re_path(r'goods/category/(?P<classes>\d)/$', views.GoodsCategoryView, name="goods_category")
]

app_name = 'product'
