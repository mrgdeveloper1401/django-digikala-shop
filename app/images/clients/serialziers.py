from rest_framework import serializers
from images.models import ImagesModel


class ImageSerialziers(serializers.HyperlinkedModelSerializer):
    product_image = serializers.CharField()
    class Meta:
        model = ImagesModel
        fields = ('image', 'product_image')