from django.shortcuts import render, redirect

# Create your views here.
def view_shoppingcart(request):
    '''A view to return the shopping bag page'''
    
    return render(request, 'shoppingcart/cart.html')


def add_to_cart(request, item_id):
    '''Add an item to the shopping cart'''
    
    # Get quantity and redirect_url from the post request
    quantity = int(request.POST['quantity'])
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
    
    # Overwrite session cart with updated version 
    request.session['cart'] = cart
    # Redirect user 
    return redirect(redirect_url)
    