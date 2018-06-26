from rest_framework_mongoengine import serializers
from rest_framework.serializers import DateTimeField

from .models import DirectCampaignReport, MetrikaSourceSummaryReport


class DirectCampaignReportSerializer(serializers.DocumentSerializer):
    date = DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = DirectCampaignReport
        exclude = ('id',)


class MetrikaSourceSummaryReportSerializer(serializers.DocumentSerializer):
    date = DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = MetrikaSourceSummaryReport
        exclude = ('id',)
