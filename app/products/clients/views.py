from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from products.models import SallerModel, Option, ProductAttributeModel, ProductLine \
 , ProductModel, ProductAttributeValueModel
from .serializers import SallerSerializer, OptionModelSerializer, ProductAttributeModelSerializer \
, ProductLineSerializer, ProductModelSerializer
from products.permission import IsOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class SallerModelViewSet(ModelViewSet):
    queryset = SallerModel.objects.all()
    serializer_class = SallerSerializer
    permission_classes = (IsOwner, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class OptionModelViewSet(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionModelSerializer
    permission_classes = (IsOwner, )


class ProductAttributeModelViewSet(ModelViewSet):
    queryset = ProductAttributeModel.objects.all()
    serializer_class = ProductAttributeModelSerializer
    permission_classes = (IsOwner, )


class ProductLineModelViewSet(ModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer
    permission_classes = (IsOwner, )


class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsOwner, )