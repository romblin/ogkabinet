from django.db import models
from django.conf import settings

from kabinet.common.models import AbstractNamedModel
from kabinet.common.fields import (
    OptionalForeignKey, OptionalManyToManyField, OptionalCharField, OptionalBigIntegerField,
    OptionalArrayField, OptionalDateTimeField, MaxOptionalCharField, OptionalPositiveIntegerField
)


class PhoneCall(models.Model):
    # uiscom fields
    called_at = OptionalDateTimeField(verbose_name='Дата/Время звонка')
    duration = OptionalPositiveIntegerField(verbose_name='Длительность звонка в секундах')
    is_answered = models.BooleanField(verbose_name='Звонок принят?', default=False)
    contact_phone_number = MaxOptionalCharField(verbose_name='Номер абонента')
    virtual_phone_number = MaxOptionalCharField(verbose_name='Виртуальный номер')
    scenario_name = MaxOptionalCharField(verbose_name='Название сценария')
    employee_name = MaxOptionalCharField(verbose_name='Имя сотруника')
    employee_id = OptionalBigIntegerField(verbose_name='ID сотрудника')
    tags = OptionalArrayField(base_field=models.CharField(max_length=255), verbose_name='Тэги')
    campaign_name = MaxOptionalCharField(verbose_name='Рекламная кампания')
    session_id = OptionalBigIntegerField(verbose_name='ID сессии звонка')
    records_ids = OptionalArrayField(
        base_field=models.CharField(max_length=255), verbose_name='ID ссылок на записанный разговор')

    # kabinet fields
    created_at = models.DateTimeField(verbose_name='Дата/время создания', auto_now_add=True)
    assigned_to = OptionalManyToManyField(
        settings.AUTH_USER_MODEL, related_name='assigned_calls', related_query_name='assigned_call',
        verbose_name='Кому был распределен звонок'
    )
    listened_by = OptionalManyToManyField(
        settings.AUTH_USER_MODEL, related_name='listened_calls', related_query_name='listened_call',
        verbose_name='Кто прослушал'
    )
    listened_at = OptionalDateTimeField(verbose_name='Дата/время прослушивания')
    complex = OptionalForeignKey(
        'realty.Complex', verbose_name='Комплекс', related_name='calls', related_query_name='calls',
        on_delete=models.SET_NULL
    )
    complex_redirected_to = OptionalForeignKey(
        'realty.Complex', verbose_name='Комплекс в отчет', on_delete=models.SET_NULL,
        related_name='redirected_calls', related_query_name='redirected_call'
    )
    company = OptionalForeignKey(
        'realty.Company', verbose_name='Застройщик', limit_choices_to={'is_ad_agency': False, 'is_agency': False},
        on_delete=models.SET_NULL, related_name='calls', related_query_name='call'
    )
    ad_agency = OptionalForeignKey(
        'realty.Company', on_delete=models.SET_NULL, verbose_name='Рекламное агенство',
        limit_choices_to={'is_ad_agency': True}, related_name='ad_agency_calls',
        related_query_name='ad_agency_calls'
    )
    realty_agency_redirected_to = OptionalForeignKey(
        'realty.Company', verbose_name='Перенаправление звонка в агенство недвижимости',
        related_name='redirected_to_agency_calls', related_query_name='redirected_to_agency_call',
        limit_choices_to={'is_agency': True}
    )
    status = OptionalForeignKey('calls.PhoneCallStatus', verbose_name='Статус звонка')
    is_caller_male = models.NullBooleanField('Звонящий мужчина?')
    realty_type = OptionalForeignKey(
        'realty.RealtyType', verbose_name='Тип недвижимости', related_name='calls',  related_query_name='call')
    rooms_counts = OptionalManyToManyField(
        'realty.RoomsCount', verbose_name='Комнатность', related_name='calls', related_query_name='call')
    areas = OptionalManyToManyField(
        'realty.Area', verbose_name='Площадь', related_name='calls', related_query_name='call')
    price = OptionalBigIntegerField(verbose_name='Цена')
    purchase_conditions = OptionalManyToManyField(
        'realty.PurchaseCondition', verbose_name='Условия покупки', related_name='calls', related_query_name='call')
    markers = OptionalManyToManyField(
        'calls.Marker', verbose_name='Доп. маркеры', related_name='calls', related_query_name='call')
    caller_actions = OptionalManyToManyField(
        'calls.CallerAction', verbose_name='Действия звонящего', related_name='calls', related_query_name='call')
    is_manager_free = models.BooleanField('Менеджер свободен', default=False)
    speech_tags = OptionalManyToManyField(
        'calls.SpeechTag', related_name='calls', related_query_name='call', verbose_name='Речь')
    answer_tags = OptionalManyToManyField(
        'calls.AnswerTag', related_name='calls', related_query_name='call', verbose_name='Ответы на вопросы')
    manager_name = OptionalCharField(verbose_name='Имя менеджера', max_length=255)
    transaction_status = OptionalForeignKey(
        'calls.TransactionStatus', related_name='calls', related_query_name='call', verbose_name='Статус сделки')
    main_source = OptionalForeignKey('calls.MainSource', verbose_name='Основной источник')
    additional_source = OptionalForeignKey('calls.AdditionalSource', verbose_name='Доп. источник')

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'
        get_latest_by = 'called_at'


class PhoneCallStatus(AbstractNamedModel):

    class Meta:
        verbose_name = 'Статус звонка'
        verbose_name_plural = 'Статусы звонков'


class CallerAction(AbstractNamedModel):

    class Meta:
        verbose_name = 'Действие звонящего'
        verbose_name_plural = 'Действия звонящих'


class SpeechTag(AbstractNamedModel):

    class Meta:
        verbose_name = 'Речь'
        verbose_name_plural = 'Речь'


class AnswerTag(AbstractNamedModel):

    class Meta:
        verbose_name = 'Ответ на вопросы'
        verbose_name_plural = 'Ответы на вопросы'


class TransactionStatus(AbstractNamedModel):

    class Meta:
        verbose_name = 'Статус сделки'
        verbose_name_plural = 'Статусы сделок'


class Marker(AbstractNamedModel):

    class Meta:
        verbose_name = 'Маркер'
        verbose_name_plural = 'Маркеры'


class MainSource(AbstractNamedModel):
    class Meta:
        verbose_name = 'Основной источник'
        verbose_name_plural = 'Основные источники'


class AdditionalSource(AbstractNamedModel):
    class Meta:
        verbose_name = 'Доп. источник'
        verbose_name_plural = 'Доп. источники'
