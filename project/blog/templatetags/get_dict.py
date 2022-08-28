from django import template

register= template.Library()
@register.filter(name="get_dict")
def get_dict(dict,key):
    return dict.get(key)