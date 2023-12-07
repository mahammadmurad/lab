from django.shortcuts import render, get_object_or_404
from . models import *
from category.models import *

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_avialable=True)
    else:
        products = Product.objects.filter(is_avialable=True)
    context = {
        'products':products,}
    
    return render(request, 'store/store.html', context)
