from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from apps.reports.services import create_direct_campaign_report_from_api
from kabinet.services.yandex.direct import get_campaign_performance_report
from apps.realty.models import YaDirectCampaign


class Command(BaseCommand):
    help = 'Выгружает отчет из Я.Директа за последнюю неделю'

    def handle(self, *args, **options):
        campaigns = YaDirectCampaign.objects.all()

        cids = [str(c.number) for c in campaigns]
        cids_types = {str(c.number): c.get_type_display() for c in campaigns}

        today = datetime.today()

        for i in range(7):
            date_from = today - timedelta(days=i + 1)
            date_to = today - timedelta(days=i)
            for item in get_campaign_performance_report(cids, date_from, date_to):
                create_direct_campaign_report_from_api(item, cids_types[item['CampaignId']])

