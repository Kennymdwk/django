from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    all_products = Product.objects.all()
    return render(request, 'products/index.html', {'all_products': all_products})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})
