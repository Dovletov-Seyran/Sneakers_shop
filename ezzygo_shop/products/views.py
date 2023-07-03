from rest_framework import viewsets

from .serializers import ProductSerializer, CategorySerializer, SizeSerializer, GenderSerializer,OrderSerialiser
from .models import Product, Category, Size, Gender, Order

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_by = 5

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    paginate_by = 5

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    pagination_by = 5

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    paginate_by = 5

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialiser
    paginate_by = 5