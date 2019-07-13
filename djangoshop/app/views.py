from django.shortcuts import render
from app.models import Category, Product


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', context)  # Отправляем в base.html
