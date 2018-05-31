from django.utils.crypto import get_random_string

from transliterate import slugify

from apps.kauth.services import create_user
from .models import Company, Complex


def create_or_update_company(cid: int, name: str, is_ad_agency: bool = False, is_agency: bool = False) -> None:
    defaults = {'name': name, 'is_ad_agency': is_ad_agency, 'is_agency': is_agency}
    c, created = Company.objects.update_or_create(id=cid, defaults=defaults)

    if created:
        slugged_name = slugify(name, 'ru')
        user = create_user(slugged_name, get_random_string(8), first_name=name)
        user.companies.add(c)


def create_or_update_complex(cid: int, name: str, subdomain: str = None) -> None:
    Complex.objects.update_or_create(id=cid, defaults={'name': name, 'subdomain': subdomain})
