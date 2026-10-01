from .models import Products,Order,OrderItem
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields = "__all__"
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("Price Must be greater Than 0")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product','quantity','order_total_price')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = ('order_id','user','order_at','status','items')