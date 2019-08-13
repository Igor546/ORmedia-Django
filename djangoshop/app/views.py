from django.shortcuts import render
from app.models import Category, Product, CartItem, Cart
from django.http import HttpResponseRedirect
from django.urls import reverse


# Главная
def base_view(request):
    # Работа с корзиной
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    products = Product.objects.all()
    notebooks = Product.objects.notebooks()
    context = {
        'categories': categories,
        'products': products,
        'notebooks': notebooks,
        'cart': cart
    }
    return render(request, 'base.html', context)  # Отправляем в base.html


# Просмотр по категориям
def product_view(request, product_slug):
    # Работа с корзиной
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'categories': categories,
        'product': product,
        'cart': cart
    }
    return render(request, 'product.html', context)


# Просмотр по продуктам
def category_view(request, category_slug):
    # Работа с корзиной
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()  # Дописал сам
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'categories': categories,  # Дописал сам
        'category': category,
        'products_of_category': products_of_category,
        'cart': cart
    }
    return render(request, 'category.html', context)


# Корзина
def cart_view(request):
    # Работа с корзиной
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()  # Дописал сам
    context = {
        'categories': categories,  # Дописал сам
        'cart': cart
    }
    return render(request, 'cart.html', context)


# Как я понял этот метод мы регистрируем в urls под именем "add_to_cart" и потом используем в HTML "product.html"
# и должны будем передать аргумент "product_slug"
def add_to_cart_view(request, product_slug):
    # Работа с корзиной
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart(product.slug)
    return HttpResponseRedirect(reverse('cart'))


def del_to_cart_view(request, product_slug):
    # Работа с корзиной
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.del_to_cart(product.slug)
    return HttpResponseRedirect(reverse('cart'))
