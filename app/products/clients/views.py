from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from products.models import Option, ProductAttributeModel, ProductLine \
 , ProductModel, ProductAttributeValueModel
from .serializers import OptionModelSerializer, ProductAttributeModelSerializer \
, ProductLineSerializer, ProductModelSerializer
from products.permission import IsOwner
from django.db import connection
from django.db import reset_queries


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

    
class ProductModelViewSet(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.select_related()
    serializer_class = ProductModelSerializer
    permission_classes = (IsOwner, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'company_warrent_name', 'saller')
    search_fields = ('product_name', )

    def retrieve(self, request, *args, **kwargs):
        reset_queries()
        responce = super().retrieve(request, *args, **kwargs)
        print(len(connection.queries))
        return responce


