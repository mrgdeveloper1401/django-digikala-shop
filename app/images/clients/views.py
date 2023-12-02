from rest_framework.viewsets import ReadOnlyModelViewSet
from images.models import Image
from .serialziers import ImageSerialziers


class ImagesViewSet(ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerialziers