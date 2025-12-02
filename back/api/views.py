from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Ambiente, Sensor, Historico
from .serializers import AmbienteSerializer, SensorSerializer, HistoricoSerializer



class AmbienteViewSet(viewsets.ModelViewSet):  # Garante que só usuario logados mexem nos ambientes 
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes = [IsAuthenticated]


class SensorViewSet(viewsets.ModelViewSet): # Filtros por query params
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'ambiente']


    # PATCH - Alternar o status de um sensor 
    @action(detail=True, methods=['patch'])  # Permite Alternar status do sensor
    def alterar_status(self, request, pk=None):
        sensor = self.get_object()
        sensor.status = not sensor.status
        sensor.save()

        return Response({
            'id': sensor.id,
            'status_atual': sensor.status,
            'mensagem': 'Status alterado com sucesso.'
        })


    # GET - Sensores ativos
    @action(detail=False, methods=['get']) 
    def ativos(self, request):
        sensores = Sensor.objects.filter(status=True)
        serializer = self.get_serializer(sensores, many=True)
        
        return Response(serializer.data)


    # GET - Sensores inativos
    @action(detail=False, methods=['get'])
    def inativos(self, request):
        sensores = Sensor.objects.filter(status=False)
        serializer = self.get_serializer(sensores, many=True)
        
        return Response(serializer.data)


    # GET - Sensores filtrados por ambiente
    @action(detail=False, methods=['get'])
    def por_ambiente(self, request):
        ambiente_id = request.query_params.get("ambiente")
        sensores = Sensor.objects.filter(ambiente_id=ambiente_id)
        serializer = self.get_serializer(sensores, many=True)
        
        return Response(serializer.data)



class HistoricoViewSet(viewsets.ModelViewSet): # permite retornar as medições daquele sensor
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor', 'ambiente', 'timestamp']

    # GET - Histórico de um sensor específico
    @action(detail=False, methods=['get'])
    def do_sensor(self, request):
        sensor_id = request.query_params.get("sensor")
        historico = Historico.objects.filter(sensor_id=sensor_id)
        serializer = self.get_serializer(historico, many=True)
        
        return Response(serializer.data)
