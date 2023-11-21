from rest_framework import serializers
from products.models import SallerModel
from products.models import Option, ProductAttributeModel, ProductAttributeValueModel \
  , ProductLine, ProductModel

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

class SallerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    class Meta:
        model = SallerModel
        exclude = (
            'slug',
            'created_at',
            'updated_at',
            'id'
        )

        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        return SallerModel.objects.create(**validated_data)
    


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = (
            'created_at',
            'updated_at',
            'id',
            'is_active',
        )


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = (
            'created_at',
            'updated_at',
            'id',
            'is_active',
        )