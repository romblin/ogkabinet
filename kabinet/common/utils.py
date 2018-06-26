from datetime import datetime

from django.utils.safestring import mark_safe


def humanize_bool(value: bool) -> str:
    return {False: 'Нет', True: 'Да'}[value]


def build_promosite_url(subdomain: str) -> str:
    return 'https://{}.ongrad.ru/'.format(subdomain)


def promosite_link(subdomain: str):
    if not subdomain:
        return None
    else:
        return mark_safe('<a href="{url}" target="_blank">{url}</a>'.format(url=build_promosite_url(subdomain)))


def date_to_datetime(date):
    return datetime(date.year, date.month, date.day, 0, 0, 0, 0)
