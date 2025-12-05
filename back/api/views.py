from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from datetime import timedelta

from .models import Ambiente, Sensor, Historico,Local,Responsavel
from .serializers import AmbienteSerializer, SensorSerializer, HistoricoSerializer, LocalSerializer,ResponsavelSerializer


# =====================================================================
# AmbienteViewSet 
# Garante que só usuários autenticados mexam nos ambientes
# =====================================================================
class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes = [IsAuthenticated]



# =====================================================================
# SensorViewSet
# =====================================================================
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'ambiente', 'tipo']


    # PATCH - Alternar status do sensor
    @action(detail=True, methods=['patch'])
    def alterar_status(self, request, pk=None):
        sensor = self.get_object()

        sensor.status = "INATIVO" if sensor.status == "ATIVO" else "ATIVO"
        sensor.save()

        return Response({
            "id": sensor.id,
            "status_atual": sensor.status,
            "mensagem": "Status alterado com sucesso."
        })


    # GET - Sensores ativos
    @action(detail=False, methods=['get'])
    def ativos(self, request):
        sensores = Sensor.objects.filter(status="ATIVO")
        serializer = self.get_serializer(sensores, many=True)
        return Response(serializer.data)


    # GET - Sensores inativos
    @action(detail=False, methods=['get'])
    def inativos(self, request):
        sensores = Sensor.objects.filter(status="INATIVO")
        serializer = self.get_serializer(sensores, many=True)
        return Response(serializer.data)


    # GET - Sensores filtrados por ambiente
    @action(detail=False, methods=['get'])
    def por_ambiente(self, request):
        ambiente_id = request.query_params.get("ambiente")
        sensores = Sensor.objects.filter(ambiente_id=ambiente_id)
        serializer = self.get_serializer(sensores, many=True)
        return Response(serializer.data)



# =====================================================================
# HistoricoViewSet
# =====================================================================
class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor', 'ambiente', 'timestamp']


    # Histórico de um sensor específico
    @action(detail=False, methods=['get'])
    def do_sensor(self, request):
        sensor_id = request.query_params.get("sensor")
        historico = Historico.objects.filter(sensor_id=sensor_id)
        serializer = self.get_serializer(historico, many=True)
        return Response(serializer.data)


    # Últimas X horas
    @action(detail=False, methods=['get'])
    def recentes(self, request):
        horas = int(request.query_params.get("hours", 24))
        limite = timezone.now() - timedelta(hours=horas)

        historico = Historico.objects.filter(timestamp__gte=limite)
        serializer = self.get_serializer(historico, many=True)
        return Response(serializer.data)
    
    
    def create(self, request, *args, **kwargs):
        # Pega o ID do sensor enviado
        sensor_id = request.data.get("sensor_id")

        # Verifica se o sensor existe
        try:
            sensor = Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return Response(
                {"erro": "Sensor não encontrado"},
                status=404
            )

        # Bloqueia criação se sensor estiver inativo
        if sensor.status == "INATIVO":
            return Response(
                {"erro": "Sensor inativo. Medição não permitida"},
                status=400
            )

        # Valida o serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Cria o objeto
        self.perform_create(serializer)

        return Response(serializer.data, status=201)


# =====================================================================
# LocalViewSet
# =====================================================================
class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def sensores(self, request, pk=None):
        sensores = Sensor.objects.filter(ambiente__local_id=pk)
        serializer = SensorSerializer(sensores, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def medicoes(self, request, pk=None):
        historico = Historico.objects.filter(sensor__ambiente__local_id=pk)
        serializer = HistoricoSerializer(historico, many=True)
        return Response(serializer.data)


# =====================================================================
# ResponsavelViewSet
# =====================================================================
class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    permission_classes = [IsAuthenticated]

  