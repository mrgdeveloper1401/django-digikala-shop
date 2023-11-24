from rest_framework.viewsets import ReadOnlyModelViewSet
from images.models import ImagesModel
from .serialziers import ImageSerialziers


class ImagesViewSet(ReadOnlyModelViewSet):
    queryset = ImagesModel.objects.all()
    serializer_class = ImageSerialziers