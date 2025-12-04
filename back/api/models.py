from django.db import models

# ================================================================
# Choices oficiais
# ================================================================

TIPO_SENSOR = [
    ('TEMP', 'Temperatura'),
    ('UMI', 'Umidade'),
    ('ILUM', 'Iluminação'),
    ('CONT', 'Contador'),
]

UNIDADE_MEDIA = [
    ('C', '°C'),
    ('P', '%'),
    ('LX', 'Lux'),
    ('N', 'Número'),
]

STATUS_SENSOR = [
    ('ATIVO', 'Ativo'),
    ('INATIVO', 'Inativo'),
]


# ================================================================
# Modelo: Responsável
# Cada responsável cuida de 1 ambiente
# ================================================================
class Responsavel(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# ================================================================
# Modelo: Local
# Local físico da escola: laboratório, pátio, corredor, etc.
# ================================================================
class Local(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# ================================================================
# Modelo: Ambiente
# Um ambiente pertence a um local e tem um responsável
# ================================================================
class Ambiente(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True)
    descricao = models.CharField(max_length=100)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


# ================================================================
# Modelo: Sensor
# Cada sensor tem tipo, mac, unidade de medida e está em um ambiente
# ================================================================
class Sensor(models.Model):
    tipo = models.CharField(max_length=20, choices=TIPO_SENSOR)
    mac_address = models.CharField(max_length=17, unique=True)
    unidade_media = models.CharField(max_length=8, choices=UNIDADE_MEDIA)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_SENSOR, default='ATIVO')
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.mac_address}"


# ================================================================
# Modelo: Histórico de medições
# Guarda os valores coletados por sensor
# ================================================================
class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.tipo} - {self.valor} - {self.timestamp}"
