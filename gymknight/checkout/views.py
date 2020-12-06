from django.shortcuts import get_object_or_404, render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import OrderForm
from products.models import Product
from .models import Order, OrderLineItem
from django.conf import settings
import stripe
import json

from shoppingcart.contexts import shopppingcart_contents

# Handle saving info to user accounts
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'There has been an error processing'
                       ' your payment. Please try again later')
        return HttpResponse(content=e, status=400)

def checkout(request):
    '''View to return the checkout app'''
    # Get stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY   
    
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city_or_town': request.POST['city_or_town'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            pid = request.POST.get('client_secret').split('_secret')[0]
            order = order_form.save(commit=False)
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We couldn't find that product in our databse."
                        "Please contact us via email to let us know.")
                    )
                    order.delete()
                    return redirect(reverse('view_shoppingcart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('successful_checkout', args=[order.order_no]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check all fields and try again.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "You have no items in your cart.")
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
        messages.warning(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    
    return render(request, template, context)

def successful_checkout(request, order_no):
    '''View to be displayed once payment has been completed successfully'''
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_no=order_no)
    messages.success(request, f'You order has been successfully processed \
        Your order number is {order_no}. A confirmation \
        email will be sent to your email: {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/successful_checkout.html'
    context = {
        'order': order,
    }

    return render(request, template, context)