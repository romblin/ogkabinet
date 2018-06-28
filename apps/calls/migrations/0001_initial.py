# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kabinet.common.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realty', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Ответ на вопросы',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
        migrations.CreateModel(
            name='CallerAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Действие звонящего',
                'verbose_name_plural': 'Действия звонящих',
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Маркер',
                'verbose_name_plural': 'Маркеры',
            },
        ),
        migrations.CreateModel(
            name='PhoneCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('called_at', kabinet.common.fields.OptionalDateTimeField(blank=True, null=True, verbose_name='Дата/Время звонка')),
                ('duration', kabinet.common.fields.OptionalPositiveIntegerField(blank=True, null=True, verbose_name='Длительность звонка в секундах')),
                ('is_answered', models.BooleanField(default=False, verbose_name='Звонок принят?')),
                ('contact_phone_number', kabinet.common.fields.MaxOptionalCharField(blank=True, max_length=255, null=True, verbose_name='Номер абонента')),
                ('virtual_phone_number', kabinet.common.fields.MaxOptionalCharField(blank=True, max_length=255, null=True, verbose_name='Виртуальный номер')),
                ('scenario_name', kabinet.common.fields.MaxOptionalCharField(blank=True, max_length=255, null=True, verbose_name='Название сценария')),
                ('employee_name', kabinet.common.fields.MaxOptionalCharField(blank=True, max_length=255, null=True, verbose_name='Имя сотруника')),
                ('employee_id', kabinet.common.fields.OptionalBigIntegerField(blank=True, null=True, verbose_name='ID сотрудника')),
                ('tags', kabinet.common.fields.OptionalArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='Тэги')),
                ('campaign_name', kabinet.common.fields.MaxOptionalCharField(blank=True, max_length=255, null=True, verbose_name='Рекламная кампания')),
                ('session_id', kabinet.common.fields.OptionalBigIntegerField(blank=True, null=True, verbose_name='ID сессии звонка')),
                ('records_ids', kabinet.common.fields.OptionalArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='ID ссылок на записанный разговор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата/время создания')),
                ('listened_at', kabinet.common.fields.OptionalDateTimeField(blank=True, null=True, verbose_name='Дата/время прослушивания')),
                ('is_caller_male', models.NullBooleanField(verbose_name='Звонящий мужчина?')),
                ('price', kabinet.common.fields.OptionalBigIntegerField(blank=True, null=True, verbose_name='Цена')),
                ('is_manager_free', models.BooleanField(default=False, verbose_name='Менеджер свободен')),
                ('manager_name', kabinet.common.fields.OptionalCharField(blank=True, max_length=255, null=True, verbose_name='Имя менеджера')),
                ('ad_agency', kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ad_agency_calls', related_query_name='ad_agency_calls', to='realty.Company', verbose_name='Рекламное агенство')),
                ('answer_tags', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='calls', related_query_name='call', to='calls.AnswerTag', verbose_name='Ответы на вопросы')),
                ('areas', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='calls', related_query_name='call', to='realty.Area', verbose_name='Площадь')),
                ('assigned_to', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='assigned_calls', related_query_name='assigned_call', to=settings.AUTH_USER_MODEL, verbose_name='Кому был распределен звонок')),
                ('caller_actions', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='calls', related_query_name='call', to='calls.CallerAction', verbose_name='Действия звонящего')),
                ('company', kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calls', related_query_name='call', to='realty.Company', verbose_name='Застройщик')),
                ('complex', kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calls', related_query_name='calls', to='realty.Complex', verbose_name='Комплекс')),
                ('complex_redirected_to', kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirected_calls', related_query_name='redirected_call', to='realty.Complex', verbose_name='Комплекс в отчет')),
                ('listened_by', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='listened_calls', related_query_name='listened_call', to=settings.AUTH_USER_MODEL, verbose_name='Кто прослушал')),
                ('markers', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='calls', related_query_name='call', to='calls.Marker', verbose_name='Доп. маркеры')),
                ('purchase_conditions', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='calls', related_query_name='call', to='realty.PurchaseCondition', verbose_name='Условия покупки')),
                ('realty_agency_redirected_to', kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redirected_to_agency_calls', related_query_name='redirected_to_agency_call', to='realty.Company', verbose_name='Перенаправление звонка в агенство недвижимости')),
                ('realty_type', kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calls', related_query_name='call', to='realty.RealtyType', verbose_name='Тип недвижимости')),
                ('rooms_counts', kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='calls', related_query_name='call', to='realty.RoomsCount', verbose_name='Комнатность')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
                'get_latest_by': 'called_at',
            },
        ),
        migrations.CreateModel(
            name='PhoneCallStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Статус звонка',
                'verbose_name_plural': 'Статусы звонков',
            },
        ),
        migrations.CreateModel(
            name='SpeechTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Речь',
                'verbose_name_plural': 'Речь',
            },
        ),
        migrations.CreateModel(
            name='TransactionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Статус сделки',
                'verbose_name_plural': 'Статусы сделок',
            },
        ),
        migrations.AddField(
            model_name='phonecall',
            name='speech_tags',
            field=kabinet.common.fields.OptionalManyToManyField(blank=True, related_name='calls', related_query_name='call', to='calls.SpeechTag', verbose_name='Речь'),
        ),
        migrations.AddField(
            model_name='phonecall',
            name='status',
            field=kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calls.PhoneCallStatus', verbose_name='Статус звонка'),
        ),
        migrations.AddField(
            model_name='phonecall',
            name='transaction_status',
            field=kabinet.common.fields.OptionalForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calls', related_query_name='call', to='calls.TransactionStatus', verbose_name='Статус сделки'),
        ),
    ]