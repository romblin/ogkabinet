from functools import update_wrapper

from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from apps.ogrealty.models import OGCompany, OGComplex
from apps.realty.services import create_or_update_complex, create_or_update_company

if settings.STAGING:
    site_header = 'Тестовый кабинет'
elif settings.PRODUCTION:
    site_header = 'Кабинет'
else:
    site_header = 'Кабинет (разработка)'


class KabinetAdminSite(AdminSite):
    site_header = site_header
    site_title = 'Ongrad.ru'
    index_title = 'Кабинет'

    def message_user(self, request, message, level=messages.INFO, extra_tags='',
                     fail_silently=False):
        if not isinstance(level, int):
            # attempt to get the level if passed a string
            try:
                level = getattr(messages.constants, level.upper())
            except AttributeError:
                levels = messages.constants.DEFAULT_TAGS.values()
                levels_repr = ', '.join('`%s`' % l for l in levels)
                raise ValueError('Bad message level string: `%s`. '
                                 'Possible values are: %s' % (level, levels_repr))

        messages.add_message(request, level, message, extra_tags=extra_tags, fail_silently=fail_silently)

    def get_urls(self):
        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            wrapper.admin_site = self
            return update_wrapper(wrapper, view)

        return super().get_urls() + [
            url(r'^load-companies/$', wrap(self.load_companies), name='load-companies'),
            url(r'^load-complexes/$', wrap(self.load_complexes), name='load-complexes'),
        ]

    def load_complexes(self, request, *args, **kwargs):
        og_complexes = OGComplex.objects.all()

        for oc in og_complexes:
            create_or_update_complex(oc.id, oc.short_name, oc.promosite_domain)

        self.message_user(request, 'Комплексы успешно созданы')

        return HttpResponseRedirect(reverse('admin:realty_complex_changelist'))

    def load_companies(self, request, *args, **kwargs):
        og_companies = OGCompany.objects.all().prefetch_related('types')

        for oc in og_companies:
            create_or_update_company(oc.id, oc.name, oc.is_ad_agency, oc.is_agency)

        self.message_user(request, 'Компании успешно созданы')

        return HttpResponseRedirect(reverse("admin:realty_company_changelist"))

site = KabinetAdminSite()

site.register(Group, GroupAdmin)
site.register(Permission)
