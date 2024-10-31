from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_list(request):
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {'categories': categories})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})
