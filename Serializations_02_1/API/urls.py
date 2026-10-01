from .views import get_all_products,product_detail,order_list
from django.urls import path

urlpatterns = [
    path("products/",get_all_products,name="get_all_products"),
    path("products/<int:id>/",product_detail,name="product_detail"),
    path("orders/",order_list,name="order_list")
]