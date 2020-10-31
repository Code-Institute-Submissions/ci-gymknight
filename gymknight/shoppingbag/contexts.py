from django.conf import settings
from decimal import Decimal

def shopppingbag_contents(request):
    
    shoppingbag_items = []
    total = 0
    product_count = 0
    
    if total < settings.FREE_DELIVERY_MINIMUM:
        delivery_charge = Decimal(settings.STD_DELIVERY_CHARGE)
        free_delivery_delta = total - settings.FREE_DELIVERY_MINIMUM
    else:
        delivery_charge = 0
        free_delivery_delta = 0
        
    grand_total = delivery_charge + total
        
    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': 'total',
        'grand_total': grand_total,
        'delivery_charge': delivery_charge,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_minimum': settings.FREE_DELIVERY_MINIMUM,
        'standard_delivery_charge': settings.STD_DELIVERY_CHARGE
    }
    
    context = {}
    return context
