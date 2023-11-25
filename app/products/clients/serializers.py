from rest_framework import serializers
from products.models import ProductAttributeModel, ProductAttributeValueModel \
  , ProductLineModel, ProductModel
from Category.client.serialziers import CategorySerialziers
from sallers.clients.serialzers import GenuinSallerSerializer


class ProductAttributeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeModel
        fields = ('attr',)
        
class ProductAttributeValueSerialziers(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValueModel
        fields = ('attr_value', 'product')

class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLineModel
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
