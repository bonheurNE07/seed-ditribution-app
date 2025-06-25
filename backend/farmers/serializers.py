from rest_framework import serializers
from .models import Farmer, Species, SeedDistribution, Cell, Village

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = "__all__"

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = "__all__"

class VillegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = "__all__"

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = "__all__"

class SeedDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeedDistribution
        fields = "__all__"

