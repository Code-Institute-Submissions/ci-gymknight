from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings
import stripe

from shoppingcart.contexts import shopppingcart_contents

# Create your views here.

def checkout(request):
    '''View to return the checkout app'''
    # Get stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY    
    # Get cart from session
    cart = request.session.get('cart', {})
    # If there is no products return error message
    if not cart:
        messages.error(request, "You have no products in your bag.")
        return redirect(reverse('products'))
    
    current_shoppingcart = shopppingcart_contents(request)
    total = current_shoppingcart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    order_form = OrderForm()

    # check for public key
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    
    return render(request, template, context)