from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerialziers, ProductLineSerializer, ProductImageSerizliers
from products.models import ProductModel, ProductLineModel, ProductImage
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerialziers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'brand')
    # search_fields = ('product_name', )
    

class ProductLineViewSet(ReadOnlyModelViewSet):
    queryset = ProductLineModel.objects.all()
    serializer_class = ProductLineSerializer

    
class ProductImageViewSet(ReadOnlyModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerizliers
    