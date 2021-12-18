import csv

from api.models import Ingredient
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load ingredients data to DB'

    def handle(self, *args, **options):
        with open('/code/api/management/commands/ingredients.csv',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                name, measurement_unit = row
                Ingredient.objects.get_or_create(
                    name=name,
                    measurement_unit=measurement_unit)
