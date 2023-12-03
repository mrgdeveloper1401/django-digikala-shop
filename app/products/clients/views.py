from rest_framework.viewsets import ReadOnlyModelViewSet
from products.clients.serializers import ProductSerializer, ProductLineSerilizer, AttributeValueSerialziers, AttributeSerialziers
from products.models import Product, ProductLine, Attribute, AttributeValue
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('category', 'brand')
    lookup_field = 'slug'
            


class ProductLineViewSet(ReadOnlyModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerilizer


class AttributeViewSet(ReadOnlyModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerialziers


class AttributeValueViewSet(ReadOnlyModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerialziers