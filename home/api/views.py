from rest_framework import viewsets
from home.models import CarbonFootprint
from .serializers import CarbonFootprintSerializer

class CarbonFootprintViewSet(viewsets.ModelViewSet):
    queryset = CarbonFootprint.objects.all()
    serializer_class = CarbonFootprintSerializer
