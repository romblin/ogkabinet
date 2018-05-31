from datetime import datetime, timedelta, time
from operator import itemgetter

import pytz
from django.conf import settings

from kabinet.services.uiscom import get_calls_report
from .models import PhoneCall


def create_call(**fields) -> PhoneCall:
    return PhoneCall.objects.create(**fields)


def load_calls_from_uiscom() -> None:
    now = datetime.now(pytz.utc).astimezone(settings.MOSCOW_TIMEZONE)

    try:
        datetime_from = PhoneCall.objects.filter(called_at__isnull=False).latest().called_at
    except (AttributeError, PhoneCall.DoesNotExist):
        datetime_from = now - timedelta(days=30)

    datetime_till = datetime.combine(now.date(), time(hour=23, minute=59, second=59, tzinfo=settings.MOSCOW_TIMEZONE))

    report_fields = ['start_time', 'finish_time', 'is_lost', 'contact_phone_number', 'virtual_phone_number',
                     'scenario_name', 'employees', 'campaign_name', 'tags']
    report = get_calls_report(datetime_from, datetime_till, report_fields)

    for call_session in report:
        start_time = datetime.strptime(call_session['start_time'], settings.ISO8601_FORMAT)
        called_at = settings.MOSCOW_TIMEZONE.localize(start_time)

        finish_time = datetime.strptime(call_session['finish_time'], settings.ISO8601_FORMAT)
        finished_at = settings.MOSCOW_TIMEZONE.localize(finish_time)

        duration = finished_at - called_at
        employees = call_session['employees']
        if employees:
            employee = employees[0]
            employee_name = employee['employee_full_name']
            employee_id = employee['employee_id']
        else:
            employee_name = None
            employee_id = None

        if call_session['tags']:
            tags = [t['tag_name'] for t in call_session['tags']]
        else:
            tags = None

        fields = {
            'called_at': called_at,
            'duration': int(duration.total_seconds()),
            'is_answered': not call_session['is_lost'],
            'contact_phone_number': call_session['contact_phone_number'],
            'virtual_phone_number': call_session['virtual_phone_number'],
            'scenario_name': call_session['scenario_name'],
            'employee_name': employee_name,
            'employee_id': employee_id,
            'campaign_name': call_session['campaign_name'],
            'tags': tags
        }

        create_call(**fields)
