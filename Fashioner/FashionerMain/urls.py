from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.products, name='home'),
    # path('home/logout/',TemplateView.as_view(template_name='registration/logout.html'), name='logout'),
    path('checkout/', TemplateView.as_view(template_name='checkout-page.html'), name='checkout'),
    path('product/<pid>/', views.product_page, name='products'),
    path('cart/', TemplateView.as_view(template_name='cart-page.html'), name='cart'),
    path('wishlist/', TemplateView.as_view(template_name='wishlist-page.html'), name='wishlist'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('category/', TemplateView.as_view(template_name='category-page.html'), name='category'),
]
