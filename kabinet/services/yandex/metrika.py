import requests
from django.conf import settings

STATS_DATA_BASE_URL = 'https://api-metrika.yandex.ru/stat/v1/data'


def get_sources_summary(sources_ids, date_from=None, date_to=None) -> list:
    params = {
        'oauth_token': settings.YANDEX_API_TOKEN,
        'preset': 'sources_summary',
        'ids': ','.join(map(str, sources_ids)),
        'date1': date_from.strftime('%Y-%m-%d'),
        'date2': date_to.strftime('%Y-%m-%d')
    }
    res = requests.get(STATS_DATA_BASE_URL, params)
    json = res.json()
    return json['data']
