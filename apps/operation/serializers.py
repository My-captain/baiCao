from rest_framework import serializers

from .models import Favorite, Purchase, Generation


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = "__all__"


