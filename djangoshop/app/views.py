from django.shortcuts import render
from app.models import Category, Product


# Главная
def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    notebooks = Product.objects.notebooks()
    context = {
        'categories': categories,
        'products': products,
        'notebooks': notebooks
    }
    return render(request, 'base.html', context)  # Отправляем в base.html


# Просмотр по категориям
def product_view(request, product_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'categories': categories,
        'product': product
    }
    return render(request, 'product.html', context)


# Просмотр по продуктам
def category_view(request, category_slug):
    categories = Category.objects.all()  # Дописал сам
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'categories': categories,  # Дописал сам
        'category': category,
        'products_of_category': products_of_category
    }
    return render(request, 'category.html', context)
