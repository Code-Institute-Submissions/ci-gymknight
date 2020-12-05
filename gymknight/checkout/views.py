from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    '''View to return the checkout app'''
    # Get cart from session
    cart = request.session.get('cart', {})
    # If there is no products return error message
    if not cart:
        messages.error(request, "You have no products in your bag.")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HssThEa2dUbR51THmTD2geGbetSyi0Bt36vlNdLz7E9klfKmVBARcIToLR9aI0v43agTNCPMITeQOWrhRYcA4Dd00NKY0iumN',
        'client_secret': 'sk_test_51HssThEa2dUbR51TpoUGZUSPeVe21nZHEsB6kA80RmFRwnoPozSYgJmCtpC06xRsz1vcYQAZN4stsKTF9mP65iip00C4dyt12k',
    }

    return render(request, template, context)
    
