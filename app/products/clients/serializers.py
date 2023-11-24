from rest_framework import serializers
from products.models import Option, ProductAttributeModel, ProductAttributeValueModel \
  , ProductLine, ProductModel
from Category.client.serialziers import CategorySerialziers
from sallers.clients.serialzers import GenuinSallerSerializer
from images.clients.serialziers import ImageSerialziers


class OptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('title',)

class ProductAttributeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeModel
        fields = (
            'title',
            'product',
        )

class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = (
            'price',
            'is_stock',
            'is_delivery',
            'number_product',
        )


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategorySerialziers(read_only=True,)
    product_lines = ProductLineSerializer(many=True,)
    saller = GenuinSallerSerializer()
    name = serializers.CharField(source='product_name',)
    warrenty = serializers.CharField(source='company_warrent_name',)
    images = serializers.ImageField()
    class Meta:
        model = ProductModel
        fields = (
            'category',
            'images',
            'name',
            'description_product',
            'warrenty',
            'product_lines',
            'saller',
        )