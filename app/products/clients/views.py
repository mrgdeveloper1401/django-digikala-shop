from rest_framework.viewsets import ReadOnlyModelViewSet
from products.clients.serializers import ProductSerializer, ProductLineSerilizer
from products.models import Product, ProductLine


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductLineViewSet(ReadOnlyModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerilizer