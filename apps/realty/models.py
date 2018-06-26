from django.db import models
from django.conf import settings

from kabinet.common.models import AbstractNamedModel
from kabinet.common.fields import MaxOptionalCharField, OptionalManyToManyField, OptionalBigIntegerField


class Complex(AbstractNamedModel):
    subdomain = MaxOptionalCharField(verbose_name='Поддомен')
    metrika_source_id = OptionalBigIntegerField(verbose_name='Счетчик Я.Метрики')

    class Meta:
        verbose_name = 'Комплекс'
        verbose_name_plural = 'Комплексы'


class YaDirectCampaign(models.Model):
    number = models.BigIntegerField(verbose_name='Номер')
    type = models.CharField(verbose_name='Тип', choices=(('search', 'Поисковая'), ('rsya', 'РСЯ')), max_length=255)
    complex = models.ForeignKey(
        'Complex', verbose_name='Комплекс', on_delete=models.CASCADE, related_name='ya_direct_campaigns')

    class Meta:
        verbose_name = 'Номер кампании в Я.Директе'
        verbose_name_plural = 'Номера кампаний в Я.Директе'

    def __str__(self):
        return str(self.number)


class RealtyType(AbstractNamedModel):

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'


class RoomsCount(AbstractNamedModel):

    class Meta:
        verbose_name = 'Комнатность'
        verbose_name_plural = 'Комнатности'


class Area(AbstractNamedModel):

    class Meta:
        verbose_name = 'Площадь'
        verbose_name_plural = 'Площади'


class PurchaseCondition(AbstractNamedModel):

    class Meta:
        verbose_name = 'Условие покупки'
        verbose_name_plural = 'Условия покупки'


class Company(AbstractNamedModel):
    is_ad_agency = models.BooleanField('Рекламное агенство', default=False)
    is_agency = models.BooleanField('Агенство недвижимости', default=False)
    users = OptionalManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Пользователи', related_name='companies')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
