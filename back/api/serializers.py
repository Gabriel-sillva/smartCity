from rest_framework import serializers
from .models import Ambiente, Sensor, Historico, Local, Responsavel


# =====================================================================
# Serializador de Local
# =====================================================================
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['id', 'nome']


# =====================================================================
# Serializador de Responsável
# =====================================================================
class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['id', 'nome']


# =====================================================================
# Serializador de Ambiente
# =====================================================================
class AmbienteSerializer(serializers.ModelSerializer):
    local = LocalSerializer(read_only=True)
    local_id = serializers.PrimaryKeyRelatedField(
        queryset=Local.objects.all(),
        source="local",
        write_only=True
    )

    responsavel = ResponsavelSerializer(read_only=True)
    responsavel_id = serializers.PrimaryKeyRelatedField(
        queryset=Responsavel.objects.all(),
        source="responsavel",
        write_only=True
    )

    class Meta:
        model = Ambiente
        fields = [
            'id',
            'descricao',
            'local',
            'local_id',
            'responsavel',
            'responsavel_id'
        ]


# =====================================================================
# Serializador de Sensor
# =====================================================================
class SensorSerializer(serializers.ModelSerializer):
    ambiente = AmbienteSerializer(read_only=True)
    ambiente_id = serializers.PrimaryKeyRelatedField(
        queryset=Ambiente.objects.all(),
        source='ambiente',
        write_only=True
    )

    class Meta:
        model = Sensor
        fields = [
            'id',
            'tipo',
            'mac_address',
            'unidade_media',
            'latitude',
            'longitude',
            'status',
            'ambiente',
            'ambiente_id',
            'criado_em'
        ]


# =====================================================================
# Serializador de Histórico
# =====================================================================
class HistoricoSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True)
    sensor_id = serializers.PrimaryKeyRelatedField(
        queryset=Sensor.objects.all(),
        source="sensor",
        write_only=True
    )

    ambiente = AmbienteSerializer(read_only=True)
    ambiente_id = serializers.PrimaryKeyRelatedField(
        queryset=Ambiente.objects.all(),
        source="ambiente",
        write_only=True
    )

    class Meta:
        model = Historico
        fields = [
            'id',
            'sensor',
            'sensor_id',
            'ambiente',
            'ambiente_id',
            'valor',
            'timestamp'
        ]
