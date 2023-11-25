from rest_framework import serializers
from products.models import ProductAttributeModel, ProductAttributeValueModel \
  , ProductLineModel, ProductModel, BrandModel
from Category.client.serialziers import CategorySerialziers
from sallers.clients.serialzers import GenuinSallerSerializer
from images.clients.serialziers import ImageSerialziers


class ProductAttributeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeModel
        fields = ('attr','description')


class ProductAttributeValueSerialziers(serializers.ModelSerializer):
    attribute = ProductAttributeModelSerializer(many=False)
    class Meta:
        model = ProductAttributeValueModel
        fields = ('attr_value', 'attribute')


class BrandSerialziers(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ('brand_name',)


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategorySerialziers(read_only=True,)
    saller = GenuinSallerSerializer()
    brand = BrandSerialziers(many=False,)
    class Meta:
        model = ProductModel
        fields = (
            'category',
            'saller',
            'brand',
            'product_name',
            'description_product',
        )


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLineModel
        fields = (
            'upc',
            'price',
            'is_stock',
            'is_delivery',
            'number_product',
            'attribute_value'
        )
