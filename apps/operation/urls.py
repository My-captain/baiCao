from django.urls import path, re_path
from operation import views

urlpatterns = [
    re_path(r'purchase/$', views.PurchaseView.as_view(), name="purchase"),
    re_path(r'favorite/list/$', views.FavoriteListView.as_view(), name="favorite_list"),
    re_path(r'generation/$', views.GenerationView.as_view(), name="generation")
]

app_name = 'operation'
