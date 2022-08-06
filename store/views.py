from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})



def categories(request):
    return {
        'categories': Category.objects.all()
    }
