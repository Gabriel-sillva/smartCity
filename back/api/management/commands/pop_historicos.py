import csv
from django.core.management.base import BaseCommand
from api.models import Sensor, Ambiente, Historico
from datetime import datetime

class Command(BaseCommand):
    help = "Importa dados históricos de sensores a partir de um arquivo CSV"

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Caminho do arquivo CSV')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']

        try:
            with open(file_path, encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)

                count = 0
                for row in reader:
                    sensor_mac = row['sensor_mac']
                    valor = float(row['valor'])
                    timestamp_str = row['timestamp']
                    ambiente_id = int(row['ambiente'])

                    # Buscar sensor
                    try:
                        sensor = Sensor.objects.get(mac_address=sensor_mac)
                    except Sensor.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f"Sensor não encontrado: {sensor_mac}"))
                        continue

                    # Buscar ambiente
                    try:
                        ambiente = Ambiente.objects.get(id=ambiente_id)
                    except Ambiente.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f"Ambiente não encontrado: {ambiente_id}"))
                        continue

                    # Converter timestamp
                    try:
                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f"Timestamp inválido: {timestamp_str}"))
                        continue

                    # Criar histórico
                    Historico.objects.create(
                        sensor=sensor,
                        ambiente=ambiente,
                        valor=valor,
                        timestamp=timestamp
                    )

                    count += 1
                    self.stdout.write(self.style.SUCCESS(f"Histórico criado: {sensor_mac} -> {valor}"))

                self.stdout.write(self.style.SUCCESS(f"\nImportação de históricos concluída! Total: {count}"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Arquivo não encontrado: {file_path}"))
