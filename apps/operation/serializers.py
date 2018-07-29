from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Favorite, Purchase, Generation


class PurchaseSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Purchase
        exclude = ['add_time']


class FavoriteSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Favorite

        validators = [
            UniqueTogetherValidator(
                queryset=Purchase.objects.all(),
                fields=('customer', 'goods'),
                message="您已收藏过该商品，请不要重复收藏啊智障"
            )
        ]

        exclude = ['add_time']


class GenerationSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Generation
        exclude = ['add_time']


