from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SpeciesViewSet, DistributionCreateView, 
                    FarmerViewSet, CellViewSet, VillageViewSet,
                    lookup_farmer_by_qr)

router = DefaultRouter()
router.register(r'species', SpeciesViewSet)
router.register(r'farmers', FarmerViewSet)
router.register(r'cells', CellViewSet)
router.register(r'villages', VillageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lookup_farmer_by_qr/', lookup_farmer_by_qr, name='lookup_farmer'),
    path('distributions/create/', DistributionCreateView.as_view(), name='create_distribution'),
]
