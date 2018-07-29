from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from .serializers import NewsSerializer, BaseSerializer, StaffSerializer
from .models import News, Base, Staff

# ================

from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer
from random import choice
from rest_framework import status
from .models import VerifyCode
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication
from rest_framework import permissions
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from utils.send_sms_aliyun import aliyun_send_sms

# Create your views here.

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    用户自定义验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 如果抛了异常那么不再向下执行、返回400错误
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]

        code = self.generate_code()
        sms_status = aliyun_send_sms(code=code, mobile=mobile)

        if sms_status["Code"] != "OK":
            # send failed
            return Response({
                "mobile": sms_status["Message"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # send success
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)


class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # 注册后立刻生成该user的token
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


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
