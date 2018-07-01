from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from transliterate import slugify

from apps.profiles.services import create_user_profile
from .models import Company, Complex


def create_or_update_company(
        cid: int,
        name: str,
        is_ad_agency: bool = False,
        is_agency: bool = False,
        is_builder: bool = False) -> None:
    defaults = {'name': name, 'is_ad_agency': is_ad_agency, 'is_agency': is_agency, 'is_builder': is_builder}
    c, created = Company.objects.update_or_create(id=cid, defaults=defaults)

    if created:
        slugged_name = slugify(name, 'ru')
        user = get_user_model().objects.create_user(slugged_name, None, get_random_string(0))
        user.companies.add(c)
        create_user_profile(user, name)


def create_or_update_complex(cid: int, name: str, subdomain: str = None) -> None:
    Complex.objects.update_or_create(id=cid, defaults={'name': name, 'subdomain': subdomain})
