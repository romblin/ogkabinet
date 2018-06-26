from django.forms.widgets import Widget

from .utils import promosite_link


class LinkWidget(Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return promosite_link(value) if value else '-'
