from rest_framework import serializers
from .models import Product, User, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

    def validate(self, attrs):

        price = attrs.get("price")
        stock = attrs.get("stock")

        if price < 0:
            raise serializers.ValidationError("Price cannot be negative.")

        if stock < 0:
            raise serializers.ValidationError("Stock cannot be negative.")

        if stock == 0 and price != 0:
            raise serializers.ValidationError("Price must be 0 when stock is 0.")

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "date_joined"]


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(
        max_digits=15, decimal_places=3, read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "total_price"]


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["order_id", "status", "order_at", "user", "items"]
