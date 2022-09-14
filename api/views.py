import random
import time

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.models import Product
from api.serializers import ProductSerializer


def index(response):
    return render(response, "api/index.html")


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer


def change_product1_name(request):
    for _ in range(1, 1000):
        product1 = Product.objects.get(pk=1)
        product1.quantity = random.randint(1, 500)
        product1.save()
        time.sleep(0.2)
    return HttpResponse("<h1>calculating</h1>")