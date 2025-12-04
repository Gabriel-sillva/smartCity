import csv
import os
from django.core.management.base import BaseCommand
from api.models import Ambiente, Local, Responsavel

class Command(BaseCommand):
    help = "Popula a tabela Ambiente a partir de um arquivo CSV"

    def add_arguments(self, parser):
        parser.add_argument("--file", type=str, required=True, help="Caminho do arquivo CSV")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file"]

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Arquivo não encontrado: {file_path}"))
            return

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            next(reader)  # Pula cabeçalho: local,descricao,responsavel

            for row in reader:
                local_id = int(row[0].strip())
                descricao = row[1].strip()
                responsavel_id = int(row[2].strip())

                try:
                    local = Local.objects.get(id=local_id)
                    responsavel = Responsavel.objects.get(id=responsavel_id)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erro ao carregar IDs: {e}"))
                    continue

                obj, created = Ambiente.objects.get_or_create(
                    descricao=descricao,
                    local=local,
                    responsavel=responsavel
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Ambiente criado: {descricao}"))
                else:
                    self.stdout.write(f"Ambiente já existia: {descricao}")

        self.stdout.write(self.style.SUCCESS("Importação de ambientes concluída!"))
