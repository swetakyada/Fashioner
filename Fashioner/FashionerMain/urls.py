from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('home/', views.products, name='home'),
    path('home/logout',TemplateView.as_view(template_name='registration/logout.html'), name='logout'),
    path('home/checkout/', TemplateView.as_view(template_name='checkout-page.html'), name='checkout'),
    path('home/products/', TemplateView.as_view(template_name='product-page.html'), name='products'),
    path('home/cart/', TemplateView.as_view(template_name='cart-page.html'), name='cart'),
    path('home/wishlist/', TemplateView.as_view(template_name='wishlist-page.html'), name='wishlist'),
]
