from django import template

register = template.Library()


@register.filter(name='columns')
def get_columns(value):
    b = value.values_list(named=True)
    return b


@register.filter(name='row')
def get_row(value, arg):
    result = 'value.{}'.format(arg)
    return eval(result)
