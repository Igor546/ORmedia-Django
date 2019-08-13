from django.shortcuts import render
from app.models import Category, Product, CartItem, Cart
from django.http import HttpResponseRedirect


# Главная
def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    notebooks = Product.objects.notebooks()
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'products': products,
        'notebooks': notebooks,
        'cart': cart
    }
    return render(request, 'base.html', context)  # Отправляем в base.html


# Просмотр по категориям
def product_view(request, product_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'product': product,
        'cart': cart
    }
    return render(request, 'product.html', context)


# Просмотр по продуктам
def category_view(request, category_slug):
    categories = Category.objects.all()  # Дописал сам
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    cart = Cart.objects.first()
    context = {
        'categories': categories,  # Дописал сам
        'category': category,
        'products_of_category': products_of_category,
        'cart': cart
    }
    return render(request, 'category.html', context)


# Корзина
def cart_view(request):
    categories = Category.objects.all()  # Дописал сам
    cart = Cart.objects.first()
    context = {
        'categories': categories,  # Дописал сам
        'cart': cart
    }
    return render(request, 'cart.html', context)


# Как я понял этот метод мы регистрируем в urls под именем "add_to_cart" и потом используем в HTML "product.html"
# и должны будем передать аргумент "product_slug"
def add_to_cart_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, price=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
    return HttpResponseRedirect('/cart/')
