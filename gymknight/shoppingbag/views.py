from django.shortcuts import render

# Create your views here.
def view_shoppingbag(request):
    '''A view to return the shopping bag page'''
    
    return render(request, 'shoppingbag/bag.html')
