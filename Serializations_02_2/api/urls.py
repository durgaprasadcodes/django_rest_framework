from django.urls import path
from .views import ProductListView, OrderListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="ProductListView"),
    path("orders/", OrderListView.as_view(), name="OrderListView"),
]
