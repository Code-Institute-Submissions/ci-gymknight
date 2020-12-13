from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_shoppingcart(request):
    '''A view to return the shopping cart page'''
    
    return render(request, 'shoppingcart/cart.html')

def add_to_cart(request, item_id):
    '''Add an item to the shopping cart'''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        # If size add item with 'items_by size'
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                # If such size exists update quantity
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Quantity of {product.name} in size {size.upper()} has been updated in your cart')
            else:
                # If not then add specified quantity
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
    # Else do the same as above but without "items_by_size"
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Quantity of {product.name} has been updated in your cart')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    # Override session cart item with updated version
    request.session['cart'] = cart
    # Redirect user back to the same url
    return redirect(redirect_url)


def update_cart(request, item_id):
    '''Update an item in the shopping cart'''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        # If size update item within 'items_by size' if quanit is over 0
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Quantity of {product.name} in size {size.upper()} has been updated in your cart')
        else:
            # Else it will be deleted
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
    else:
        # Else for items without size
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Quantity of {product.name} has been updated in your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')
    
    # Override session cart item with updated version
    request.session['cart'] = cart
    # redirect user back to view shopping cart
    return redirect(reverse('view_shoppingcart'))

def remove_item(request, item_id):
    '''Remove item from the cart'''

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            # if there is size delete item from items_by_size
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
        else:
            # Else if items have no size
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        # Override session cart item with updated version
        request.session['cart'] = cart
        return HttpResponse(status=200)
    # Raise exception if there is an error
    except Exception as e:
        messages.error(request, f'Error removing product from your cart')
        return HttpResponse(status=500)