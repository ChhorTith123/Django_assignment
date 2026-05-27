from django.shortcuts import render
from .models import Category, Brand, Product


# Create your views here.
def category(request):
    categories = Category.objects.all()

    context= {'categories': categories}
    return render(request, 'category.html', context)

def brand(request):
    brands = Brand.objects.all()

    context= {'brands': brands}
    return render(request, 'brand.html', context)

def product(request):
    products = Product.objects.all()

    context= {'products': products}
    return render(request, 'product.html', context)