from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.products, name='home'),
    path('product', views.product_page, name='products'),
    path('cproduct', views.cproduct, name='cproduct'),
    path('cart', views.user_cart, name='cart'),
    path('wishlist', views.user_wishlist, name='wishlist'),
    path('addtowishlist', views.add_to_wishlist, name='addtowishlist'),
    path('removefromwishlist', views.remove_from_wishlist, name='removefromwishlist'),
    path('profile/', views.profile_page, name='profile'),
    path('category/<cid>', views.category_page, name='category'),
    path('addtocart',views.add_to_cart, name="addtocart"),
    path('removefromcart', views.remove_from_cart, name="removefromcart"),
    path('updatecartitem', views.update_cart_item, name="updatecratitem"),
    path('checkout', views.checkout, name='checkout'),
    path('placeorder', views.place_order, name="placeorder"),
]
