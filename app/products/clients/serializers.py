from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Product, ProductLine, Attribute, AttributeValue
from Category.client.serialziers import CategorySerialziers, BrandSerilizer
from images.clients.serialziers import ImageSerialziers


class AttributeSerialziers(ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('name', 'description', )


class AttributeValueSerialziers(ModelSerializer):
    attribute = AttributeSerialziers(many=True)
    class Meta:
        model = AttributeValue
        fields = ('attribute_value', 'attribute')


class ProductLineSerilizer(ModelSerializer):
    attribute_value = AttributeValueSerialziers(many=True)
    class Meta:
        model = ProductLine
        fields = (
            'price',
            'stock_quantity',
            'attribute_value'
        )


class ProductSerializer(ModelSerializer):
    category = CategorySerialziers()
    brand = BrandSerilizer()
    product_line_products = ProductLineSerilizer(many=True)
    image = serializers.ImageField(source='product_image_products')
    class Meta:
        model = Product
        fields = (
            'category',
            'brand',
            'image',
            'product_name',
            'product_line_products',
        )
