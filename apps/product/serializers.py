from rest_framework import serializers

from users.serializers import BaseSerializer
from .models import Goods, Plants


class GoodsSerializer(serializers.ModelSerializer):
    base = BaseSerializer()

    class Meta:
        model = Goods
        fields = "__all__"


class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = "__all__"
