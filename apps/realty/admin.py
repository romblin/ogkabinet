from django.contrib import admin
from django.utils.safestring import mark_safe

from kabinet.common.admin import site
from kabinet.common.utils import humanize_bool, build_promosite_url
from .models import *

site.register((RealtyType, RoomsCount, Area, PurchaseCondition,))


@admin.register(Complex, site=site)
class ComplexAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    readonly_fields = ('name', 'subdomain')
    list_display = ('name', 'promosite_url')
    list_display_links = None

    def promosite_url(self, obj):
        if not obj.subdomain:
            return None
        return mark_safe('<a href="{url}" target="_blank">{url}</a>'.format(url=build_promosite_url(obj.subdomain)))
    promosite_url.short_description = 'Промосайт'


@admin.register(Company, site=site)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    readonly_fields = ('name', 'is_agency', 'is_ad_agency')
    list_filter = ('is_agency', 'is_ad_agency')
    filter_horizontal = ('users',)
    list_display = ('name', 'is_company_agency', 'is_company_ad_agency')

    def is_company_ad_agency(self, obj):
        return humanize_bool(obj.is_ad_agency)
    is_company_ad_agency.short_description = 'Рекламное агенство'

    def is_company_agency(self, obj):
        return humanize_bool(obj.is_agency)
    is_company_agency.short_description = 'Агенство недвижимости'
