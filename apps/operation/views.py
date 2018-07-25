from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json

from .models import Purchase, Favorite, Generation
from .serializers import PurchaseSerializer, FavoriteSerializer, GenerationSerializer

# Create your views here.


class PurchaseView(APIView):
    def get(self, request):
        purchase = Purchase.objects.all()[:10]
        purchase_serializer = PurchaseSerializer(purchase, many=True)
        return Response(purchase_serializer.data)

    def post(self, request):
        purchases = request.POST["purchases"]
        print(purchases)
        serializer = PurchaseSerializer(data=json.loads(purchases))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GenerationView(APIView):
    def get(self, request):
        generation = Generation.objects.all()[:10]
        generation_serializer = GenerationSerializer(generation, many=True)
        return Response(generation_serializer.data)

    def post(self, request):
        generation = request.POST["generation"]
        print(generation)
        serializer = GenerationSerializer(data=json.loads(generation))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)


class FavoriteListView(APIView):
    def get(self, request):
        favorite = Favorite.objects.all()[:10]
        favorite_serializer = FavoriteSerializer(favorite, many=True)
        return Response(favorite_serializer.data)

    def post(self, request):
        favorite = request.POST["favorite"]
        print(favorite)
        serializer = FavoriteSerializer(data=json.loads(favorite))
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

