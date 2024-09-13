from rest_framework import viewsets
from .models import DadosSensor
from .serializers import DadosSensorSerializer

class DadosSensorViewSet(viewsets.ModelViewSet):
    queryset = DadosSensor.objects.all()
    serializer_class = DadosSensorSerializer
