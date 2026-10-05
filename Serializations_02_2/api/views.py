from django.shortcuts import render
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# @api_view(["GET"])
# def product_list(request):

#     products = Product.objects.all()
#     serializer = ProductSerializer(products,many=True)

#     return Response(serializer.data)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)

        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product, many=True).data, status=201)
        return Response(serializer.errors, status=400)


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)
