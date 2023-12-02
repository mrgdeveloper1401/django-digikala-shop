from rest_framework import serializers
from images.models import Image


class ImageSerialziers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('image', )