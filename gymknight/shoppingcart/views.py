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
    cart = request.session.get('cart', {})
    
    # If item id in cart - increase quantity, if not add it to cart
    if item_id in list (cart.keys()):
        cart[item_id] += quantity
    else: 
        cart[item_id] = quantity
    
    # Overwrite session cart with updated version 
    request.session['cart'] = cart
    # Redirect user 
    print(request.session['cart'])
    return redirect(redirect_url)
    