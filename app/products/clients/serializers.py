from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Product, ProductLine
from Category.client.serialziers import CategorySerialziers, BrandSerilizer
from images.clients.serialziers import ImageSerialziers


class ProductLineSerilizer(ModelSerializer):
    class Meta:
        model = ProductLine
        fields = (
            'price',
            'stock_quantity',
        )


class ProductSerializer(ModelSerializer):
    category = CategorySerialziers()
    brand = BrandSerilizer()
    product_line_products = ProductLineSerilizer(many=True)
    class Meta:
        model = Product
        fields = (
            'category',
            'brand',
            'image',
            'product_name',
            'product_line_products',
        )
