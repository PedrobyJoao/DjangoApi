import imp
from django.shortcuts import render
from rest_framework import viewsets
from .models import Region, Fruit
from .serializer import RegionSerializer, FruitSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Region':  '/Region/, URL: http://127.0.0.1:8000/Region',
        'Fruit':  '/Fruit/, URL: http://127.0.0.1:8000/Fruit',
        'Specific Element':  "If you want to select a specific data you must use the ID after '/', example: http://127.0.0.1:8000/Fruit/3 will give you the page of a specific fruit where you can edit/delete it"
        }

    return Response(api_urls)
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class FruitViewSet(viewsets.ModelViewSet):
    serializer_class = FruitSerializer
    queryset = Fruit.objects.all()
