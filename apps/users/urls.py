from django.urls import path, re_path
from users import views


urlpatterns = [
    re_path(r'news/list/$', views.NewsListView.as_view(), name="news_list"),
    re_path(r'base/list/$', views.BaseListView.as_view(), name="base_list"),
    re_path(r'staff/list/$', views.StaffListView.as_view(), name="staff_list")
]

app_name = 'users'

