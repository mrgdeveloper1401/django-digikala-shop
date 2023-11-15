from rest_framework import serializers
from products.models import ProductModel


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        
        
class SallerSerialziers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'