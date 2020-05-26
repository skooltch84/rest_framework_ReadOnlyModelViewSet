from rest_framework import viewsets
from .serializers import DescriptionSerializer
from .models import Description


class DescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Create weather descriptions and read the info"""
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
