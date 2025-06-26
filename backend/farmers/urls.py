from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SpeciesViewSet, DistributionCreateView, 
                    FarmerViewSet, CellViewSet, VillageViewSet,
                    lookup_farmer_by_qr, farmer_distribution_history,
                    download_distribution_pdf)

router = DefaultRouter()
router.register(r'species', SpeciesViewSet)
router.register(r'farmers', FarmerViewSet)
router.register(r'cells', CellViewSet)
router.register(r'villages', VillageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('distributions/create/', DistributionCreateView.as_view(), name='create_distribution'),
    path('lookup_farmer_by_qr/', lookup_farmer_by_qr, name='lookup_farmer'),
    path('farmers/<int:farmer_id>/history/', farmer_distribution_history, name='farmer_history'),
    path('distributions/<int:distribution_id>/pdf/', download_distribution_pdf, name='distribution_pdf'),
]
