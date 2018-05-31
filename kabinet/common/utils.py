def humanize_bool(value: bool) -> str:
    return {False: 'Нет', True: 'Да'}[value]


def build_promosite_url(subdomain: str) -> str:
    return 'https://{}.ongrad.ru/'.format(subdomain)
