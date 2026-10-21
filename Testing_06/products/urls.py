from .views import ProductsApiView
from django.urls import path

urlpatterns = [
    path("products/", ProductsApiView.as_view(), name="product-list"),
    path("products/<int:id>/", ProductsApiView.as_view(), name="product-detail"),
]
