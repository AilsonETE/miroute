from rest_framework import serializers
from .models import DadosSensor

class DadosSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosSensor
        fields = '__all__'  
