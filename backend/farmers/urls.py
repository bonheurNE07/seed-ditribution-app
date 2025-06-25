from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SpeciesViewSet, SeedDistributionViewSet, 
                    FarmerViewSet, CellViewSet, VillageViewSet,
                    lookup_farmer_by_qr)

router = DefaultRouter()
router.register(r'species', SpeciesViewSet)
router.register(r'distributions', SeedDistributionViewSet)
router.register(r'farmers', FarmerViewSet)
router.register(r'cells', CellViewSet)
router.register(r'villages', VillageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lookup_farmer_by_qr/', lookup_farmer_by_qr, name='lookup_farmer'),
]
