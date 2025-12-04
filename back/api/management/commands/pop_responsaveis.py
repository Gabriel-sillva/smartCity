from django.core.management.base import BaseCommand
from api.models import Responsavel
import csv

class Command(BaseCommand):
    help = "Popula a tabela Responsavel usando um arquivo CSV."

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            help='Caminho para o arquivo CSV contendo os responsáveis.'
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs['file']

        if not csv_file:
            self.stdout.write(self.style.ERROR("Você deve informar o caminho do CSV usando --file"))
            return

        try:
            with open(csv_file, encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    nome = row.get('nome')

                    if Responsavel.objects.filter(nome=nome).exists():
                        self.stdout.write(self.style.WARNING(f"Responsável '{nome}' já existe. Pulando..."))
                        continue

                    Responsavel.objects.create(nome=nome)

                    self.stdout.write(self.style.SUCCESS(f"Responsável criado: {nome}"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Arquivo não encontrado: {csv_file}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro inesperado: {e}"))
