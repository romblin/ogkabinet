from datetime import timedelta

from django.contrib import admin

from kabinet.common.admin import site
from .models import *

site.register((CallerAction, SpeechTag, AnswerTag, TransactionStatus, PhoneCallStatus, Marker))


@admin.register(PhoneCall, site=site)
class PhoneCallAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at', 'called_at', 'duration', 'is_answered', 'contact_phone_number', 'virtual_phone_number',
        'scenario_name', 'employee_name', 'employee_id', 'tags', 'campaign_name'
    )
    list_display = (
        'called_at', 'contact_phone_number', 'human_duration', 'scenario_name', 'tags', 'campaign_name',
        'virtual_phone_number',
    )
    filter_horizontal = (
        'assigned_to', 'listened_by', 'rooms_counts', 'areas', 'purchase_conditions', 'markers',
        'caller_actions', 'speech_tags', 'answer_tags'
    )
    list_filter = ('is_answered',)
    ordering = ('-called_at',)
    search_fields = ('contact_phone_number', 'virtual_phone_number', 'scenario_name', 'tags', 'campaign_name')

    def human_duration(self, obj):
        return str(timedelta(seconds=obj.duration))
    human_duration.short_description = 'Длительность'
