from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    pass 

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=250,null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=3)
    stock = models.PositiveBigIntegerField(default=0)
    
    @property
    def check_stock(self):
        return self.stock > 0    
    def __str__(self):
        return self.name

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending"
        CONFIRMED = "Confirmed"
        CANCELLED = "cancelled"
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
    order_at = models.DateField(auto_now_add=True)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    @property
    def total_price(self):
        return self.product.price*self.quantity
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"