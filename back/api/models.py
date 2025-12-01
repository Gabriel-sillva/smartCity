from django.db import models
from django.core.exceptions import ValidationError

# Choices 

TIPO_SENSOR = [
        ('TEMP', 'Temperatura'),
        ('UMI', 'Umidade'),
        ('ILUM','Iluminação'),
        ('CONT', 'Contador'),
    ]

TIPO_UNIDADEMED = [
        ('TEM', '°C'),
        ('UMI','%'),
        ('ILUM', 'lux'),
        ('CONT', 'N°'),
    
    ]

STATUS_SENSOR = [
        ('ATIVO','Ativo'),
        ('INATIVO', 'Inativo'),
    ]


class Locais(models.Model):
    local = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.local}"


class Responsaveis(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Ambiente(models.Model):
    local = models.ForeignKey(Locais, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    responsavel = models.ForeignKey(Responsaveis, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.descricao
    


class Sensor(models.Model):
    sensor = models.CharField(max_length= 20, choices=TIPO_SENSOR)
    mac_address = models.CharField(max_length=17, unique=True)
    unidade_med = models.CharField(max_length=10, choices=TIPO_UNIDADEMED) # °C, %, lux, N°
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_SENSOR, default='ATIVO')
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.sensor} - {self.mac_address}"

    
class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.sensor.sensor} - {self.valor} - {self.timestamp}"
    



