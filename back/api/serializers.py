from rest_framework import serializers
from .models import Ambiente, Sensor, Historico

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = ['id', 'sig', 'descricao', 'ni', 'responsavel']


class SensorSerializer(serializers.ModelSerializer):
    ambiente = AmbienteSerializer(read_only=True)
    ambiente_id = serializers.PrimaryKeyRelatedField(
        queryset=Ambiente.objects.all(), 
        source='ambiente', write_only=True
    )

    class Meta:
        model = Sensor
        fields = ['id', 
                  'sensor', 
                  'mac_address', 
                  'unidade', 
                  'latitude', 
                  'longitude', 
                  'status', 
                  'ambiente', 
                  'ambiente_id']
        
class HistoricoSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True) 
    sensor_id = serializers.PrimaryKeyRelatedField(
        queryset=Sensor.objects.all(), 
        source='sensor', write_only=True
    )
    ambiente = AmbienteSerializer(read_only=True)
    ambiente_id = serializers.PrimaryKeyRelatedField(
        queryset=Ambiente.objects.all(), 
        source='ambiente', write_only=True
    )

    class Meta:
        model = Historico
        fields = ['id', 
                  'sensor', 
                  'sensor_id', 
                  'ambiente', 
                  'ambiente_id', 
                  'valor', 
                  'timestamp']