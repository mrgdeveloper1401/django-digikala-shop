from rest_framework import serializers
from images.models import ImagesModel


class ImageSerialziers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImagesModel
        fields = ('image', )