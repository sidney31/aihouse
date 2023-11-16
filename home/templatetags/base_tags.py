from home.models import ButtonSnippet

from django import template

register = template.Library()

@register.inclusion_tag('./home/tags/button.html', takes_context=True)
def button_tag(context):
    return{
        'request': context['request'],
        'button': ButtonSnippet.objects.first()
    }