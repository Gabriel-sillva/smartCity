from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Ambiente, Sensor, Historico
from .serializers import AmbienteSerializer, SensorSerializer, HistoricoSerializer


class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes =[IsAuthenticated]


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = ['status', 'ambiente']
    permission_classes =[IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def alterar_status(self, request, pk=None):
        sensor = self.get_object()
        sensor.status = not sensor.status
        sensor.save()
        return Response({'status': sensor.status})


class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes =[IsAuthenticated]
