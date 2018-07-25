from rest_framework import serializers

from .models import Goods, Plants


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"


class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = "__all__"
