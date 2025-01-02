from rest_framework import serializers
from home.models import CarbonFootprint

class CarbonFootprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonFootprint
        fields = '__all__'
