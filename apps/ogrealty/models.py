from django.db import models

from kabinet.common.models import AbstractNamedModel, ReadOnlyModelMixin


class OGComplex(ReadOnlyModelMixin, models.Model):
    short_name = models.CharField(verbose_name='Краткое название', max_length=255)
    promosite_domain = models.CharField(verbose_name='Промо домен', max_length=255)

    class Meta:
        db_table = 'realty_complex'
        managed = False

    def __str__(self):
        return self.short_name


class OGCompany(ReadOnlyModelMixin, AbstractNamedModel):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        managed = False
        db_table = 'realty_company'

    def __str__(self):
        return self.name

    @property
    def is_agency(self):
        return self.types.agencies().exists()

    @property
    def is_ad_agency(self):
        return self.types.ad_agencies().exists()


class OGCompanyQuerySet(models.QuerySet):

    def agencies(self):
        return self.filter(type_id=OGCompanyType.REALTY_AGENCY_ID)

    def ad_agencies(self):
        return self.filter(type_id=OGCompanyType.AD_AGENCY_ID)


class OGCompanyType(ReadOnlyModelMixin, models.Model):
    REALTY_AGENCY_ID = 3
    AD_AGENCY_ID = 7

    company = models.ForeignKey(
        'ogrealty.OGCompany', verbose_name='ID компании', db_column='company_id',
        related_name='types', related_query_name='type'
    )
    type_id = models.BigIntegerField(verbose_name='ID типа компании', db_column='companytype_id')

    objects = OGCompanyQuerySet.as_manager()

    class Meta:
        managed = False
        db_table = 'realty_company_types'
