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
# 开发环境下处理静态文件请求
from django.views.static import serve
from baiCao import settings
from django.urls import path, re_path

from django.conf.urls import url, include

# django文档
from rest_framework.documentation import include_docs_urls

import xadmin

# views
from users.views import SmsCodeViewset, UserViewset

# drf自带的token验证
from rest_framework.authtoken import views

# jwt的token验证
from rest_framework_jwt.views import obtain_jwt_token

# urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'codes', SmsCodeViewset, base_name="codes")
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [
    url(r'^', include(router.urls)),

    path('xadmin/', xadmin.site.urls),

    # product url
    path('product/', include('product.urls', namespace='product')),

    # operation url
    path('operation/', include('operation.urls', namespace='operation')),

    # rest_frame_work
    re_path('docs/', include_docs_urls("baiCao")),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf auth_token
    # re_path('api-token-auth/', views.obtain_auth_token),

    # jwt auth_token
    re_path(r'login/', obtain_jwt_token),

    # 配置上传文件的访问处理函数
    re_path(r'image/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
