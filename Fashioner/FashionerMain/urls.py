from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.products, name='home'),
    # path('home/logout/',TemplateView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('checkout/', TemplateView.as_view(template_name='checkout-page.html'), name='checkout'),
    path('product/', views.product_page, name='products'),
    path('cart/', views.user_cart, name='cart'),
    path('wishlist/', views.user_wishlist, name='wishlist'),
    path('product/addtowishlist', views.add_to_wishlist, name='addtowishlist'),
    path('wishlist/removefromwishlist', views.remove_from_wishlist, name='removefromwishlist'),
    path('profile/', views.profile_page, name='profile'),
    # path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('category/<cid>', views.category_page, name='category'),
    path('product/addtocart',views.add_to_cart, name="addtocart"),
    path('cart/removefromcart', views.remove_from_cart, name="removefromcart"),
    path('cart/updatecartitem', views.update_cart_item, name="updatecratitem"),
    path('cart/checkout', views.checkout, name='checkout'),
    path('cart/placeorder', views.place_order, name="placeorder")
]
