import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_frame_work_course_01.settings")
django.setup()

from .models import Product

products = [
    Product(
        name="Laptop",
        description="Gaming Laptop",
        price=75000,
        stock=10
    ),
    Product(
        name="Mouse",
        description="Wireless Mouse",
        price=1500,
        stock=50
    ),
    Product(
        name="Keyboard",
        description="Mechanical Keyboard",
        price=3000,
        stock=25
    ),
]

Product.objects.bulk_create(products)

print("Database populated successfully!")