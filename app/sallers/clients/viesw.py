from .serialzers import GenuinSallerSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from sallers.models import GenuinSaller

class GenuinSallerViewSet(ReadOnlyModelViewSet):
    queryset = GenuinSaller.objects.all()
    serializer_class = GenuinSallerSerializer
