from rest_framework.fields import DateTimeField as rfDateTimeField
from drf_mongo_filters import filters
from drf_mongo_filters.filtersets import Filterset


class DateTimeField(rfDateTimeField):

    def to_internal_value(self, value):
        return super(DateTimeField, self).to_internal_value(value + 'T00:00:00')


class DateTimeFilter(filters.DateTimeFilter):
    field_class = DateTimeField

    def make_field(self, **kwargs):
        kwargs['required'] = False
        kwargs['allow_null'] = True
        kwargs['source'] = 'date'
        return self.field_class(**kwargs)


class ReportFilterset(Filterset):
    date_from = DateTimeFilter(lookup='gte', name='date_from')
    date_to = DateTimeFilter(lookup='lte', name='date_to')
    campaign_id = filters.IntegerFilter()
