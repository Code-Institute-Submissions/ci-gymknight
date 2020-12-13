from django import template

register = template.Library()

# Register the filter
@register.filter(name='calculate_subtotal')
def calculate_subtotal(price, quantity):
    ''' Helper for calculating subtotal '''
    return price * quantity