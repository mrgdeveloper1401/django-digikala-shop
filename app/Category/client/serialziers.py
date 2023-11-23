from rest_framework import serializers
from Category.models import Category


class CategorySerialziers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='title',)
    class Meta:
        model = Category
        fields = ('category_name', )
