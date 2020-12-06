from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    '''View to display user profile'''
    profile = get_object_or_404(UserProfile, user=request.user)
    
    template = 'userprofile/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)