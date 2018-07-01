import io
import csv
import json

import requests

TOKEN = 'AQAAAAAciUCXAAUGZ1pvupB73EIIu5xMXuZzMPM'
DIRECT_API_BASE_URL = 'https://api.direct.yandex.com/json/v5/reports'


def get_campaign_performance_report(campaigns_ids, date_from, date_to):
    headers = {
        'Authorization': 'Bearer ' + TOKEN,
        'Client-Login': 'ra-ongrad',
        'processingMode': 'auto',
        'skipReportSummary': 'true'
    }

    body = {
        "params": {
            "SelectionCriteria": {
                "Filter": [{
                    "Field": "CampaignId",
                    "Operator": "IN",
                    "Values": list(map(str, campaigns_ids))
                }],
                "DateFrom": date_from.strftime('%Y-%m-%d'),
                "DateTo": date_to.strftime('%Y-%m-%d')
            },
            "FieldNames": [
                "CampaignId",
                "Date",
                "CampaignName",
                "Clicks",
                "Cost"
            ],
            "ReportName": "Campaign Performance Report",
            "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
            "DateRangeType": "CUSTOM_DATE",
            "Format": "TSV",
            "IncludeVAT": "NO",
            "IncludeDiscount": "NO"
        }
    }

    res = requests.post(DIRECT_API_BASE_URL, json.dumps(body, indent=4), headers=headers)

    # TODO: Обработка ошибок
    stream = io.StringIO(res.text)
    stream.readline()  # Пропускаем название отчета
    return csv.DictReader(stream, delimiter='\t', lineterminator='\n')
