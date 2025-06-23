from rest_framework import viewsets
from .models import Species, SeedDistribution, Cell, Farmer, Village
from .serializers import (
    SpeciesSerializer, SeedDistributionSerializer, FarmerSerializer,
    CellSerializer, VillegeSerializer)
class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillegeSerializer


class SeedDistributionViewSet(viewsets.ModelViewSet):
    queryset = SeedDistribution.objects.all()
    serializer_class = SeedDistributionSerializer