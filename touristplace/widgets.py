from django import forms
from django.forms.widgets import Widget
from django.utils.html import format_html

class StarRatingWidget(Widget):
    template_name = 'widgets/star_rating_widget.html'

    def get_context(self, name, value, attrs):
        return {
            'name': name,
            'value': value,
        }
