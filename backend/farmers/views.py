from rest_framework import viewsets
from .models import Species, SeedDistribution, Cell, Farmer, Village
from .serializers import (
    SpeciesSerializer, SeedDistributionSerializer, FarmerSerializer,
    CellSerializer, VillegeSerializer)
from rest_framework.permissions import IsAuthenticated

from permissions import IsAdmin, IsAgent

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = [IsAuthenticated, IsAdmin, IsAgent]

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated, IsAdmin, IsAgent]

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    permission_classes = [IsAuthenticated, IsAdmin, IsAgent]

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillegeSerializer
    permission_classes = [IsAuthenticated, IsAdmin, IsAgent]


class SeedDistributionViewSet(viewsets.ModelViewSet):
    queryset = SeedDistribution.objects.all()
    serializer_class = SeedDistributionSerializer
    permission_classes = [IsAuthenticated, IsAdmin, IsAgent]