from django import template
register = template.Library()
from operator import methodcaller

@register.simple_tag
def get_verbose_field_name(instance, field):
    """
    Returns verbose_name for a field.
    """
    my_getter = methodcaller('get_{}_display'.format(field))

    return my_getter(instance)