from django.db import models

class Ambiente(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=100)
    ni = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=50)

    def __str__(self):
        
        return self.descricao
    

class Sensor(models.Model):

    TIPO_SENSOR = [
        ('TEMP', 'Temperatura'),
        ('UMI', 'Umidade'),
        ('ILUM','Iluminação'),
        ('CONT', 'Contador'),
    ]


    sensor = models.CharField(max_length= 20, choices=TIPO_SENSOR)
    mac_address = models.CharField(max_length=17, unique=True)
    unidade = models.CharField(max_length=10) # C, %, lux, Num
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.BooleanField(default=True)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)

    def __str__(self):
        
        return f"{self.sensor} - {self.mac_address}"

    
class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.IntegerField()

    def __str__(self):
        
        return f"{self.sensor.sensor} - {self.valor} - {self.timestamp}"


