# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import kabinet.common.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Ответы на вопросы',
                'verbose_name': 'Ответ на вопросы',
            },
        ),
        migrations.CreateModel(
            name='CallerAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Действия звонящих',
                'verbose_name': 'Действие звонящего',
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Маркеры',
                'verbose_name': 'Маркер',
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
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата/время создания')),
                ('listened_at', kabinet.common.fields.OptionalDateTimeField(blank=True, null=True, verbose_name='Дата/время прослушивания')),
                ('is_caller_male', models.NullBooleanField(verbose_name='Звонящий мужчина?')),
                ('price', kabinet.common.fields.OptionalBigIntegerField(blank=True, null=True, verbose_name='Цена')),
                ('is_manager_free', models.BooleanField(default=False, verbose_name='Менеджер свободен')),
                ('manager_name', kabinet.common.fields.OptionalCharField(blank=True, max_length=255, null=True, verbose_name='Имя менеджера')),
            ],
            options={
                'verbose_name_plural': 'Звонки',
                'verbose_name': 'Звонок',
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
                'verbose_name_plural': 'Статусы звонков',
                'verbose_name': 'Статус звонка',
            },
        ),
        migrations.CreateModel(
            name='SpeechTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Речь',
                'verbose_name': 'Речь',
            },
        ),
        migrations.CreateModel(
            name='TransactionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Статусы сделок',
                'verbose_name': 'Статус сделки',
            },
        ),
    ]
