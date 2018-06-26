import os
from datetime import datetime, timedelta

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kabinet.settings')

import django
django.setup()

from django.conf import settings

from apps.realty.models import Complex, YaDirectCampaign
from apps.reports.services import create_direct_campaign_report_from_api, create_metrika_source_summary_report_from_api
from kabinet.services.yandex.direct import get_campaign_performance_report
from kabinet.services.yandex.metrika import get_sources_summary

app = Celery('kabinet', broker=settings.BROKER)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(name='load_calls_from_uiscom')
def load_calls_from_uiscom():
    from apps.calls.services import load_calls_from_uiscom
    load_calls_from_uiscom()


@app.task(name='load_ya_metrika_report')
def load_ya_metrika_report():
    sources_ids = Complex.objects.filter(metrika_source_id__isnull=False).values_list('metrika_source_id', flat=True)
    today = datetime.today().date()
    yesterday = today - timedelta(days=1)

    for sid in sources_ids:
        report = get_sources_summary([sid], yesterday, today)
        for item in report:
            create_metrika_source_summary_report_from_api(item, yesterday, sid)


@app.task(name='load_ya_direct_report')
def load_ya_direct_report():
    today = datetime.today().date()
    yesterday = today - timedelta(days=1)
    campaigns = YaDirectCampaign.objects.all()

    cids = [str(c.number) for c in campaigns]
    cids_types = {str(c.number): c.get_type_display() for c in campaigns}

    for item in get_campaign_performance_report(cids, yesterday, today):
        create_direct_campaign_report_from_api(item, cids_types[item['CampaignId']])
