from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from products.models import Option, ProductAttributeModel, ProductLine \
 , ProductModel, ProductAttributeValueModel
from .serializers import OptionModelSerializer, ProductAttributeModelSerializer \
, ProductLineSerializer, ProductModelSerializer
from products.permission import IsOwner
from django.db import connection


class OptionModelViewSet(ReadOnlyModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionModelSerializer
    permission_classes = (IsOwner, )


class ProductAttributeModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductAttributeModel.objects.all()
    serializer_class = ProductAttributeModelSerializer
    permission_classes = (IsOwner, )


class ProductLineModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer
    permission_classes = (IsOwner, )
    print('product line is', connection.queries)


class ProductModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsOwner, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'company_warrent_name', )
    search_fields = ('product_name', )
    print('product model is', connection.queries)
