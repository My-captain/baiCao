"""baiCao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

# django文档
from rest_framework.documentation import include_docs_urls

import xadmin

# views
# from users.views import LoginView

# drf自带的token验证
from rest_framework.authtoken import views

# jwt的token验证
from rest_framework_jwt.views import obtain_jwt_token

# urls


urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    # 登录与注册
    # re_path('^login/$', LoginView.as_view(), name="login"),
    # re_path('^register/$', RegisterView.as_view(), name="register"),

    # product url
    path('product/', include('product.urls', namespace='product')),

    # operation url
    path('operation/', include('operation.urls', namespace='operation')),

    # users url
    path('users/', include('users.urls', namespace='users')),

    # rest_frame_work
    re_path('docs/', include_docs_urls("baiCao")),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf auth_token
    re_path('api-token-auth/', views.obtain_auth_token),

    # jwt auth_token
    re_path(r'jwt_auth/', obtain_jwt_token)
]
