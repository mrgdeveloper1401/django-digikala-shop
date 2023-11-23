from sallers.models import GenuinSaller
from rest_framework.serializers import ModelSerializer


class GenuinSallerSerializer(ModelSerializer):
    class Meta:
        model = GenuinSaller
        fields = ('shop_name',)