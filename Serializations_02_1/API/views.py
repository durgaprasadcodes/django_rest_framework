from django.shortcuts import render,get_object_or_404
from .models import Products,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer,OrderSerializer

@api_view(['GET'])
def get_all_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request,id):
    product = get_object_or_404(Products, id=id)
    product_Serializer = ProductSerializer(product)
    return Response(product_Serializer.data)

@api_view(['GET'])
def order_list(request):
    objects = Order.objects.all()
    serializer = OrderSerializer(objects,many=True)
    return Response(serializer.data)

