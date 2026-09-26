from django.shortcuts import render,get_object_or_404
from .models import Products
from django.http import JsonResponse
from .serializer import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    
    serialization = ProductSerializer(products,many=True)

    return Response(serialization.data)

@api_view(['GET'])
def product_detail(request,id):
    product = get_object_or_404(Products, id=id)
    product_Serializer = ProductSerializer(product)
    return Response(product_Serializer.data)