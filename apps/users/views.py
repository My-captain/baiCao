from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from .serializers import NewsSerializer, BaseSerializer, StaffSerializer
from .models import News, Base, Staff

# Create your views here.

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    用户自定义验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class NewsListView(APIView):
    def get(self, request):
        news = News.objects.all()[:5]
        news_serializer = NewsSerializer(news, many=True)
        return Response(news_serializer.data)


class BaseListView(APIView):
    def get(self, requset):
        bases = Base.objects.all()[:5]
        base_serializer = BaseSerializer(bases, many=True)
        return Response(base_serializer.data)


class StaffListView(APIView):
    def get(self, request):
        staff = Staff.objects.all()[:5]
        staff_serializer = StaffSerializer(staff, many=True)
        return Response(staff_serializer.data)
