from datetime import datetime

from django.contrib.auth.models import User
from django.http import FileResponse
from django.utils.timezone import now
from django.utils.dateparse import parse_date
from django.db.models import Sum
from django.db.models.functions import TruncDay

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Species, Distribution, DistributedItem, Cell, Farmer, Village
from .serializers import (
    SpeciesSerializer, DistributionSerializer, FarmerSerializer,
    CellSerializer, VillegeSerializer, DistributionHistorySerializer,
    RecentFarmerSerializer, RecentDistributionSerializer)

from .permissions import IsAdmin, IsAgent

from .utils.pdf_generator import generate_distribution_pdf


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
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def farmer_distribution_history(request, farmer_id):
    try:
        farmer = Farmer.objects.get(pk=farmer_id)
        distributions = Distribution.objects.filter(farmer=farmer).order_by('-distributed_at')
        serializer = DistributionHistorySerializer(distributions, many=True)
        return Response(serializer.data)
    except Farmer.DoesNotExist:
        return Response({'error': 'Farmer not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_distribution_pdf(request, distribution_id):
    try:
        distribution = Distribution.objects.get(pk=distribution_id)
        pdf = generate_distribution_pdf(distribution)
        return FileResponse(open(pdf.name, 'rb'), content_type='application/pdf')
    except Distribution.DoesNotExist:
        return Response({'error': 'Distribution not found'}, status=404)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    today = now().date()

    total_farmers = Farmer.objects.count()
    seeds_today = DistributedItem.objects.filter(
        distribution__distributed_at__date=today
    ).aggregate(total=Sum('quantity'))['total'] or 0
    total_species = Species.objects.count()
    pending_verifications = Farmer.objects.filter(is_verified=False).count()

    return Response({
        'total_farmers': total_farmers,
        'seeds_distributed_today': seeds_today,
        'total_species': total_species,
        'pending_verifications': pending_verifications
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recent_farmers(request):
    farmes = Farmer.objects.select_related('location__cell').order_by('-registreted_at')[:10]
    serializer = RecentFarmerSerializer(farmes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recent_distributions(request):
    recent = Distribution.objects.select_related('farmer__location__cell')\
        .prefetch_related('items__species').order_by('-distributed_at')[:10]
    serializer = RecentDistributionSerializer(recent, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def distribution_calendar(request):
    # Consider the current month as default
    month_str = request.GET.get('month', datetime.now().strftime('%Y-%m'))
    year, month = map(int, month_str.split('-'))

    distributions = DistributedItem.objects.filter(
        distribution__distributed_at__year=year,
        distribution__distributed_at__month=month
    ).annotate(
        day=TruncDay('distribution__distributed_at')
    ).values('day').annotate(
        total=Sum('quantity')
    ).order_by('day')

    return Response({
        item['day'].strftime('%Y-%m-%d'): item['total']
        for item in distributions
    })
