from rest_framework import serializers
from products.models import Option, ProductAttributeModel, ProductAttributeValueModel \
  , ProductLine, ProductModel
from Category.client.serialziers import CategorySerialziers


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
    name = serializers.CharField(source='product_name',)
    warrenty = serializers.CharField(source='company_warrent_name',)
    class Meta:
        model = ProductModel
        fields = (
            'category',
            'name',
            'description_product',
            'image',
            'warrenty',
            'product_lines',
        )