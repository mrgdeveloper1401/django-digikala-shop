from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from products.models import ProductAttributeModel, ProductAttributeValueModel, ProductLineModel \
 , ProductModel, BrandModel
from .serializers import ProductAttributeModelSerializer, ProductAttributeValueSerialziers \
, ProductLineSerializer, ProductModelSerializer, BrandSerialziers
from products.permission import IsOwner
from django.db import connection
from django.db import reset_queries


class ProductAttributeModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductAttributeModel.objects.all()
    serializer_class = ProductAttributeModelSerializer
    permission_classes = (IsOwner, )


class ProductAttributeValueModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductAttributeValueModel.objects.all()
    serializer_class = ProductAttributeValueSerialziers
    permission_classes = (IsOwner, )

class ProductLineModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductLineModel.objects.all()
    serializer_class = ProductLineSerializer
    permission_classes = (IsOwner, )


class BrandViewSet(ReadOnlyModelViewSet):
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerialziers
    permission_classes = (IsOwner, )

class ProductModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.select_related()
    serializer_class = ProductModelSerializer
    permission_classes = (IsOwner, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'saller')
    search_fields = ('product_name', )

    def retrieve(self, request, *args, **kwargs):
        reset_queries()
        responce = super().retrieve(request, *args, **kwargs)
        print(len(connection.queries))
        return responce


