from django.utils import timezone
from django.conf import settings


def timezone_middleware(get_response):
    def middleware(request):
        timezone.activate(settings.MOSCOW_TIMEZONE)
        response = get_response(request)
        return response
    return middleware
