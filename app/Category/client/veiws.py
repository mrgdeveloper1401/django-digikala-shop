from rest_framework import viewsets
from Category.models import Category
from . import serialziers
from django.db import connection, reset_queries


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = serialziers.CategorySerialziers
