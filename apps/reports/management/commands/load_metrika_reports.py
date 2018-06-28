from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from apps.reports.services import create_metrika_source_summary_report_from_api
from kabinet.services.yandex.metrika import get_sources_summary
from apps.realty.models import Complex


class Command(BaseCommand):
    help = 'Выгружает отчет из Я.Метрики за последнюю неделю'

    def handle(self, *args, **options):
        sources_ids = Complex.objects.filter(metrika_source_id__isnull=False).values_list('metrika_source_id', flat=True)
        today = datetime.today()

        for i in range(7):
            date_from = today - timedelta(days=i + 1)
            date_to = today - timedelta(days=i)
            for sid in sources_ids:
                report = get_sources_summary([sid], date_from, date_to)
                for item in report:
                    create_metrika_source_summary_report_from_api(item, date_from, sid)
