from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.products, name='home'),
    # path('home/logout/',TemplateView.as_view(template_name='registration/logout.html'), name='logout'),
    path('checkout/', TemplateView.as_view(template_name='checkout-page.html'), name='checkout'),
    path('product/', views.product_page, name='products'),
    path('cart/', views.user_cart, name='cart'),
    path('wishlist/', TemplateView.as_view(template_name='wishlist-page.html'), name='wishlist'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('category/<cid>', views.category_page, name='category'),
    path('product/addtocart',views.add_to_cart, name="addtocart"),
    path('cart/removefromcart', views.remove_from_cart, name="removefromcart"),
    path('cart/updatecartitem', views.update_cart_item, name="updatecratitem"),
]
