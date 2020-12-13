from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm

def profile(request):
    '''View to display user profile'''
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated')
    
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    
    template = 'userprofile/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)

def order_history(request, order_no):
    ''' get order history for the user'''
    order = get_object_or_404(Order, order_no=order_no)

    messages.info(request, (
        f'This is a previously confirmed order number {order_no}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/successful_checkout.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)