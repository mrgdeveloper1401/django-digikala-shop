from rest_framework import viewsets
from Category.models import Category, BrandModel
from .serialziers import CategorySerialziers, BrandSerilizer
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerialziers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('title',)
    # search_fields = ('title', )
    lookup_field = 'title'


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerilizer
    lookup_field = 'brand_name'