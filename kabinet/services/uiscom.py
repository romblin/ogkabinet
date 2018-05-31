from datetime import datetime

import requests
from django.conf import settings


def get_calls_report(date_from: datetime, date_till: datetime, fields: list = None) -> list:
    req_json = {
        "jsonrpc": "2.0",
        "id": "number",
        "method": "get.calls_report",
        "params": {
            "access_token": settings.UISCOM_DATA_API_TOKEN,
            "date_from": date_from.strftime(settings.ISO8601_FORMAT),
            "date_till": date_till.strftime(settings.ISO8601_FORMAT),
        }
    }

    if fields is not None:
        req_json['params']['fields'] = fields

    res = requests.post(settings.UISCOM_DATA_API_BASE_URL, json=req_json)
    res_json = res.json()

    return res_json['result']['data']
