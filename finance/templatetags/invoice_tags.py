from django import template
import json

register = template.Library()

@register.filter
def status_class(status):
    classes = {
        'draft': 'btn-warning',
        'sent': 'btn-info',
        'paid': 'btn-success',
        'cancelled': 'btn-danger'
    }
    return classes.get(status, 'btn-secondary')

@register.filter
def choices_json(choices):
    return json.dumps(dict(choices))