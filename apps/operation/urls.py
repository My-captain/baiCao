from django.conf.urls import url, include
from .views import PurchaseViewSet, GenerationView, FavoriteView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'purchase', PurchaseViewSet)
router.register(r'generation', GenerationView)
router.register(r'fav', FavoriteView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
#
# urlpatterns = [
#     re_path(r'purchase/$', views.PurchaseView.as_view(), name="purchase"),
#     re_path(r'favorite/list/$', views.FavoriteListView.as_view(), name="favorite_list"),
#     re_path(r'generation/$', views.GenerationView.as_view(), name="generation")
# ]

app_name = 'operation'
