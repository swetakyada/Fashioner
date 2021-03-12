from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.products, name='home'),
    path('checkout/', TemplateView.as_view(template_name='checkout-page.html'), name='checkout'),
    path('products/', TemplateView.as_view(template_name='product-page.html'), name='products'),
    path('cart/', TemplateView.as_view(template_name='cart-page.html'), name='cart'),
]
