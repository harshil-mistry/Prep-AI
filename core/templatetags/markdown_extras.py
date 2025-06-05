from django import template
from django.utils.safestring import mark_safe
import markdown2

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(value, safe=False):
    if not value:
        return ""
    
    if safe:
        html = markdown2.markdown(value, safe_mode='escape')
    else:
        html = markdown2.markdown(value, extras=['fenced-code-blocks', 'tables', 'code-friendly'])
    
    # Mark the HTML as safe so Django renders it instead of escaping it
    return mark_safe(html)