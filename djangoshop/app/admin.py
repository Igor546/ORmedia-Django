from django.contrib import admin
from app.models import Category, Brand, Product, CartItem, Cart

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
