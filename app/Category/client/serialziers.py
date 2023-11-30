from rest_framework import serializers
from Category.models import Category, BrandModel


class CategorySerialziers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='title',)
    class Meta:
        model = Category
        fields = ('category_name', )


class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ('brand_name', )