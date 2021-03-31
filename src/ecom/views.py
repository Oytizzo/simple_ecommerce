from django.shortcuts import render


def store(request):
    context = {}
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
