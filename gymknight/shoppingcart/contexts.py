from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

def shopppingcart_contents(request):
    
    shoppingcart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    
    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shoppingcart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                product = get_object_or_404(Product, pk=item_id)
                product_count += quantity
                shoppingcart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
    
    if total < settings.FREE_DELIVERY_MINIMUM:
        delivery_charge = Decimal(settings.STD_DELIVERY_CHARGE)
        free_delivery_delta = settings.FREE_DELIVERY_MINIMUM - total
    else:
        delivery_charge = 0
        free_delivery_delta = 0
        
    grand_total = delivery_charge + total
        
    context = {
        'shoppingcart_items': shoppingcart_items,
        'total': total,
        'grand_total': grand_total,
        'delivery_charge': delivery_charge,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_minimum': settings.FREE_DELIVERY_MINIMUM,
        'standard_delivery_charge': settings.STD_DELIVERY_CHARGE
    }

    return context
