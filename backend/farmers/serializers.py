from rest_framework import serializers
from .models import Farmer, Species, DistributedItem, Distribution, Cell, Village

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

class DistributedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributedItem
        fields = ['species', 'quantity']

class DistributionSerializer(serializers.ModelSerializer):
    items = DistributedItemSerializer(many=True)
    
    class Meta:
        model = Distribution
        fields = ['id', 'farmer', 'agent', 'distributed_at', 'items']
        read_only_fields = ['agent', 'distributed_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        distribution = Distribution.objects.create(**validated_data)
        for item in items_data:
            DistributedItem.objects.create(distribution=distribution, **item)
        return distribution

class DistributedItemReadSerializer(serializers.ModelSerializer):
    species_name = serializers.CharField(source='species.name', read_only=True)

    class Meta:
        model = DistributedItem
        fields = ['species_name', 'quantity']

class DistributionHistorySerializer(serializers.ModelSerializer):
    items = DistributedItemReadSerializer(many=True)
    agent_name = serializers.CharField(source='agent.username', read_only=True)

    class Meta:
        model = Distribution
        fields = ['distributed_at', 'agent_name', 'items']
