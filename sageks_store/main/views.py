from django.shortcuts import render, get_object_or_404
from catalog.models import *


def homePage(request):
    return render(request, 'sageks_store/main/home.html')


def catalogPage(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sageks_store/catalog/catalog.html', context)

def productPage(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'sageks_store/catalog/product.html', context)
