from django.core.management.base import BaseCommand

from apps.calls.services import load_calls_from_uiscom


class Command(BaseCommand):
    help = 'создет записи о звонках на основе DATA API uiscom-a'

    def handle(self, *args, **options):
        load_calls_from_uiscom()
