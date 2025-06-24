from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Species, SeedDistribution, Cell, Farmer, Village
from .serializers import (
    SpeciesSerializer, SeedDistributionSerializer, FarmerSerializer,
    CellSerializer, VillegeSerializer)
from permissions import IsAdmin, IsAgent

class RegisterView(APIView):
    def post(self, request):
        email = r

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