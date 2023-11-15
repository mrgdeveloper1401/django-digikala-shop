from rest_framework import viewsets
from . import serialziers
from products.models import ProductModel


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = serialziers.CreateProductSerializer
    # permission_classes = ('', )

class SallerProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = serialziers.SallerSerialziers
    # permission_classes = ('', )