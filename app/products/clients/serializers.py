from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import ProductLineModel, ProductModel
from Category.client.serialziers import CategorySerialziers, BrandSerilizer


class ProductLineSerializer(ModelSerializer):
    class Meta:
        model = ProductLineModel
        fields = (
            'product',
            'price',
            'stock_quantity',
        )


class ProductSerialziers(ModelSerializer):
    category = CategorySerialziers()
    brand = BrandSerilizer()
    class Meta:
        model = ProductModel
        fields = (
            'category',
            'brand',
            'product_name',
        )
