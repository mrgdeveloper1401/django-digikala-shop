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
    product_name = serializers.CharField(source='product_line', read_only=True)
    class Meta:
        model = ProductLine
        exclude = (
            'created_at',
            'updated_at',
            'id',
            'is_active',
        )


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategorySerialziers(read_only=True)
    class Meta:
        model = ProductModel
        exclude = (
            'created_at',
            'updated_at',
            'id',
            'is_active',
            'slug',
            
        )