from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def shopppingcart_contents(request):

    # Initialise empty vars
    shoppingcart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            # Add product to total
            total += item_data * product.price
            # Increase product count
            product_count += item_data
            # Append it to the shoppingcart_Items
            shoppingcart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                 # Add product to total
                total += quantity * product.price
                # Increase product count
                product_count += quantity
                # Append it to the shoppingcart_Items
                shoppingcart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
                
    if total < settings.FREE_DELIVERY_MINIMUM:
        # Check if total is less than the free delivery minimum
        delivery_charge = settings.STD_DELIVERY_CHARGE
        free_delivery_delta = settings.FREE_DELIVERY_MINIMUM - total
    else:
        # If it's over then delivery is free
        delivery_charge = 0
        free_delivery_delta = 0
    
    # Grand total is items + delivery charge
    grand_total = Decimal(delivery_charge) + Decimal(total)
    
    # Define and return contexts
    context = {
        'shoppingcart_items': shoppingcart_items,
        'total': total,
        'grand_total': grand_total,
        'product_count': product_count,
        'delivery_charge': delivery_charge,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_minimum': settings.FREE_DELIVERY_MINIMUM,
    }

    return context