from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm

# Create your views here.
def all_products(request):
    '''View that returns all products in the database'''
    products = Product.objects.all()

    # Initialise all vars as none for start
    query = None
    cateogries = None
    sort = None
    direction = None

    if request.GET:
        # Check if sorting is in request
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                name = 'name'
                lower_name = name.lower()
                sort_key = 'lower_name'
                products = products.annotate(lower_name=lower_name)
            # Check if sorting direction is in request
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        # Check if category is in request
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Check if search is in request
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You must provide search term(s)")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # context
    context = {
        'products': products,
        'search_term': query,
        'current_categories': cateogries,
        'current_sorting': current_sorting,
    }
    
    # Render template and return context
    return render(request, 'products/products.html', context)



def product_details(request, product_id):
    '''View that returns detailed view of a single product'''
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    # Render template and return context
    return render(request, 'products/product_details.html', context)

def add_product(request):
    '''Add products to the webshop'''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added the product to the webshop')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'FAILED: Product not added. Please double check your form.')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)