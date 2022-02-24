"Views.py In Products App"
from django.shortcuts import render
from .models import Product


def all_products(request):
    "A view to see the store's products, including search abilities"
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
