import csv
import os
from django.core.management.base import BaseCommand
from api.models import Local

class Command(BaseCommand):
    help = "Popula a tabela Local a partir de um arquivo CSV"

    def add_arguments(self, parser):
        parser.add_argument("--file", type=str, required=True, help="Caminho do arquivo CSV")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file"]

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Arquivo não encontrado: {file_path}"))
            return

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                nome = row[0].strip()

                obj, created = Local.objects.get_or_create(nome=nome)

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Local criado: {nome}"))
                else:
                    self.stdout.write(f"Já existia: {nome}")

        self.stdout.write(self.style.SUCCESS("Importação concluída!"))
