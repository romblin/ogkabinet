from django.contrib import admin
from django.forms.fields import CharField
from django.forms.models import ModelForm

from kabinet.common.admin import site
from kabinet.common.utils import humanize_bool, promosite_link
from kabinet.common.forms import LinkWidget
from .models import *

site.register((RealtyType, RoomsCount, Area, PurchaseCondition,))


class YaDirectCampaignTabular(admin.TabularInline):
    model = YaDirectCampaign
    extra = 1


class ComplexForm(ModelForm):
    promosite_link = CharField(label='Промосайт', required=False, widget=LinkWidget)

    class Meta:
        model = Complex
        exclude = ('subdomain',)

    def __init__(self, *args, **kwargs):
        super(ComplexForm, self).__init__(*args, **kwargs)
        self.fields['promosite_link'].initial = self.instance.subdomain


@admin.register(Complex, site=site)
class ComplexAdmin(admin.ModelAdmin):
    form = ComplexForm
    search_fields = ('name',)
    readonly_fields = ('name', 'subdomain')
    list_display = ('name', lambda c: promosite_link(c.subdomain))
    inlines = (YaDirectCampaignTabular,)
    fieldsets = (
        (None, {
            'fields': ('name', 'metrika_source_id', 'promosite_link')
        }),
        ('Отчет Я.Директ', {
            'fields': (),
            'classes': ('collapse', 'direct')
        }),
        ('Отчет Я.Метрика', {
            'fields': (),
            'classes': ('collapse', 'metrika')
        })
    )

    class Media:
        js = (
            'dist/direct.js',
            'dist/metrika.js',
        )
        css = {
            'all': ('https://unpkg.com/react-day-picker/lib/style.css',)
        }


@admin.register(Company, site=site)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_agency', 'is_ad_agency', 'is_builder')
    filter_horizontal = ('users',)
    list_display = ('name', 'is_company_agency', 'is_company_ad_agency', 'is_company_builder')

    def is_company_builder(self, obj):
        return humanize_bool(obj.is_builder)
    is_company_builder.short_description = 'Застройщик'

    def is_company_ad_agency(self, obj):
        return humanize_bool(obj.is_ad_agency)
    is_company_ad_agency.short_description = 'Рекламное агенство'

    def is_company_agency(self, obj):
        return humanize_bool(obj.is_agency)
    is_company_agency.short_description = 'Агенство недвижимости'
