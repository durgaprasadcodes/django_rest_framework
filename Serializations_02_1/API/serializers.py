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
