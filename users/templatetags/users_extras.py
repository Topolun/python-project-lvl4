from django import template

register = template.Library()


@register.filter(name='row')
def get_row(value, arg):
    result = 'value.{}'.format(arg)
    return eval(result)
