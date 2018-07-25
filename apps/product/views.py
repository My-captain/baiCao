from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GoodsSerializer, PlantsSerializer
from .models import Goods, Plants

# Create your views here.


class GoodsListView(APIView):
    def get(self, request):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)


class PlantsListView(APIView):
    def get(self, request):
        plants = Plants.objects.all()[:10]
        plants_serializer = PlantsSerializer(plants, many=True)
        return Response(plants_serializer.data)


class PlantsSearchView(APIView):
    def post(self, request):
        key_word = request.POST["key_word"]
        print("key_word" + key_word)
        plants = Plants.objects.filter(name__icontains=key_word)
        plants_serializer = PlantsSerializer(plants, many=True)
        return Response(plants_serializer.data)


class PlantsCategoryView(APIView):
    def get(self, type, request):
        if type == "1":
            plants = Plants.objects.filter(classes="发散风热")
        elif type == "2":
            plants = Plants.objects.filter(classes="清热泻火")
        elif type == "3":
            plants = Plants.objects.filter(classes="利水渗湿")

        plants_serializer = PlantsSerializer(plants, many=True)
        return Response(plants_serializer.data)


class GoodsCategoryView(APIView):
    def get(self, classes, request):
        if classes == "1":
            goods = Goods.objects.filter(type="seed")
        elif classes == "2":
            goods = Goods.objects.filter(type="pot")
        elif classes == "3":
            goods = Goods.objects.filter(type="soil")
        elif classes == "4":
            goods = Goods.objects.filter(type="muck")

        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer)


