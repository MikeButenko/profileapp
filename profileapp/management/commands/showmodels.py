from django.core.management.base import BaseCommand
from django.apps import apps
from django.db.models import Count
from ...models import Profile

class Command(BaseCommand):
    help = 'command that prints all models and object counts.'

    def add_arguments(self, parser):
        parser.add_argument('strings', nargs='*', type=str)

    def handle(self, *args, **options):
        all = apps.all_models['profileapp']
        for element in all:
            self.stdout.write('models:{}'.format(element))
