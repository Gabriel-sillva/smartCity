import csv
import os
from django.core.management.base import BaseCommand
from api.models import Sensor, Ambiente

class Command(BaseCommand):
    help = "Popula a tabela de sensores a partir de um arquivo CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            required=True,
            help="Caminho para o arquivo CSV"
        )

    def handle(self, *args, **options):
        file_path = options['file']

        if not os.path.exists(file_path):
            self.stderr.write(f"Arquivo não encontrado: {file_path}")
            return

        with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:

                # corrigir BOM
                tipo_csv = row.get("sensor") or row.get("\ufeffsensor")

                if not tipo_csv:
                    self.stderr.write("Coluna 'sensor' não encontrada.")
                    continue

                texto_tipo = tipo_csv.strip().lower()
                unidade_csv = row["unidade_medida"].strip()

                tipo_map = {
                    "temperatura": "TEMP",
                    "umidade": "UMI",
                    "luminosidade": "ILUM",
                    "contador": "CONT",
                }

                tipo = tipo_map.get(texto_tipo)
                if not tipo:
                    self.stderr.write(f"Tipo inválido no CSV: {texto_tipo}")
                    continue

                unidade_map = {
                    "°c": "C",
                    "c": "C",
                    "%": "P",
                    "lux": "LX",
                    "n": "N",
                }

                unidade = unidade_map.get(unidade_csv.lower(), "N")

                status_raw = row["status"].strip().lower()
                status = "ATIVO" if status_raw in ["true", "ativo"] else "INATIVO"

                mac = row["mac_address"].strip()
                latitude = float(row["latitude"])
                longitude = float(row["longitude"])
                ambiente_id = int(row["ambiente"])

                try:
                    ambiente = Ambiente.objects.get(id=ambiente_id)
                except Ambiente.DoesNotExist:
                    self.stderr.write(f"Ambiente ID {ambiente_id} não existe! Pulando...")
                    continue

                sensor, created = Sensor.objects.get_or_create(
                    mac_address=mac,
                    defaults={
                        "tipo": tipo,
                        "unidade_media": unidade,
                        "latitude": latitude,
                        "longitude": longitude,
                        "status": status,
                        "ambiente": ambiente,
                    }
                )

                if created:
                    self.stdout.write(f"Sensor criado: {mac}")
                else:
                    self.stdout.write(f"Sensor já existia: {mac}")

        self.stdout.write(self.style.SUCCESS("Importação de sensores concluída!"))
