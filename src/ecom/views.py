from django.shortcuts import render

from .models import Product

def store(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'ecom/store.html', context)


def cart(request):
    context = {}
    return render(request, 'ecom/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'ecom/checkout.html', context)


def history(request):
    context = {}
    return render(request, 'ecom/history.html', context)
