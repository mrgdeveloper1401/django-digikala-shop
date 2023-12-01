from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import ProductLineModel, ProductModel, ProductImage
from Category.client.serialziers import CategorySerialziers, BrandSerilizer
from images.models import ImagesModel
from images.clients.serialziers import ImageSerialziers


class ProductImageSerizliers(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'image',
            'product_line'
        )


class ProductLineSerializer(ModelSerializer):
    products_image_line = ProductImageSerizliers(many=True)
    class Meta:
        model = ProductLineModel
        fields = (
            'products_image_line',
            'price',
            'stock_quantity',
        )


class ProductSerialziers(ModelSerializer):
    category = CategorySerialziers()
    brand = BrandSerilizer()
    product_lines = ProductLineSerializer(many=True)
    class Meta:
        model = ProductModel
        fields = (
            'category',
            'brand',
            'product_name',
            'slug',
            'product_lines'
        )
