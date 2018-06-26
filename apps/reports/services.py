from datetime import datetime

from kabinet.common.utils import date_to_datetime
from .models import DirectCampaignReport, MetrikaSourceSummaryReport


def create_direct_campaign_report_from_api(api_report_item, type_name):
    DirectCampaignReport.objects.create(
        campaign_id=int(api_report_item['CampaignId']),
        date=datetime.strptime(api_report_item['Date'], '%Y-%m-%d'),
        campaign_name=api_report_item['CampaignName'],
        clicks=float(api_report_item['Clicks']),
        total_cost=float(api_report_item['Cost']),
        type_name=type_name
    )


def create_metrika_source_summary_report_from_api(api_report_item, date, source_id):
    dims = api_report_item['dimensions']
    visits, users, bounce_rate, page_depth, avg_visit_duration = api_report_item['metrics']

    dim0 = dims[0]
    dim1 = dims[1]
    if dim1['id'] is None:
        name = dim0['name']
        id = dim0['id']
        group_name = None
        group_id = None
    else:
        name = dim1['name']
        id = dim1['id']
        group_id = dim0['id']
        group_name = dim0['name']

    MetrikaSourceSummaryReport.objects.create(
        source_id=source_id,
        date=date_to_datetime(date),
        rid=id,
        name=name,
        group_id=group_id,
        group_name=group_name,
        visits=visits,
        users_count=users,
        bounce_rate=bounce_rate,
        page_depth=page_depth,
        avg_visit_duration=avg_visit_duration
    )
