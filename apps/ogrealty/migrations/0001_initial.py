# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import kabinet.common.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OGCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'db_table': 'realty_company',
                'managed': False,
            },
            bases=(kabinet.common.models.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OGCompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.BigIntegerField(db_column='companytype_id', verbose_name='ID типа компании')),
            ],
            options={
                'db_table': 'realty_company_types',
                'managed': False,
            },
            bases=(kabinet.common.models.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OGComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=255, verbose_name='Краткое название')),
                ('promosite_domain', models.CharField(max_length=255, verbose_name='Промо домен')),
            ],
            options={
                'db_table': 'realty_complex',
                'managed': False,
            },
            bases=(kabinet.common.models.ReadOnlyModelMixin, models.Model),
        ),
    ]
