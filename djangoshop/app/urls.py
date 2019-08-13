from django.urls import path
from app import views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('category/<str:category_slug>/', views.category_view, name='category_detail'),
    path('product/<str:product_slug>/', views.product_view, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<str:product_slug>/', views.add_to_cart_view, name='add_to_cart'),
    path('del_to_cart/<str:product_slug>/', views.del_to_cart_view, name='del_to_cart'),
]
