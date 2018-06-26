from rest_framework_mongoengine import viewsets
from drf_mongo_filters.backend import MongoFilterBackend

from .filters import ReportFilterset
from .models import DirectCampaignReport, MetrikaSourceSummaryReport
from .serializers import DirectCampaignReportSerializer, MetrikaSourceSummaryReportSerializer


class DirectCampaignReportViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    serializer_class = DirectCampaignReportSerializer
    queryset = DirectCampaignReport.objects.all()
    filter_class = ReportFilterset
    filter_backends = (MongoFilterBackend,)


class MetrikaSourceSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    serializer_class = MetrikaSourceSummaryReportSerializer
    queryset = MetrikaSourceSummaryReport.objects.all()
    filter_class = ReportFilterset
    filter_backends = (MongoFilterBackend,)
