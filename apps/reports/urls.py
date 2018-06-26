from rest_framework_mongoengine import routers
from django.conf.urls import url, include

from .views import DirectCampaignReportViewSet, MetrikaSourceSummaryViewSet

direct_router = routers.DefaultRouter()
direct_router.register(r'campaigns-performance', DirectCampaignReportViewSet)

metrika_router = routers.DefaultRouter()
metrika_router.register(r'sources-summary', MetrikaSourceSummaryViewSet)

urlpatterns = [
    url(r'direct/', include(direct_router.urls)),
    url(r'metrika/', include(metrika_router.urls)),
]
