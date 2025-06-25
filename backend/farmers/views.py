from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Species, Distribution, Cell, Farmer, Village
from .serializers import (
    SpeciesSerializer, DistributionSerializer, FarmerSerializer,
    CellSerializer, VillegeSerializer)

from .permissions import IsAdmin, IsAgent


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

class DistributionCreateView(generics.CreateAPIView):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer
    permission_classes = [IsAuthenticated, IsAgent]  # or IsAdmin too

    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)



@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAgent, IsAdmin])
def lookup_farmer_by_qr(request):
    national_id =  request.data.get("national_id")
    try:
        farmer = Farmer.objects.get(national_id=national_id)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)
    except Farmer.DoesNotExist:
        return Response({'error': 'Farmer not found'}, status=404)