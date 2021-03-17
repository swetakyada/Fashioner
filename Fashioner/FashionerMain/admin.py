from django.contrib import admin
from .models import Category, Product, Cart, WishList, Order
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Order)


# admin.site.site_header ="FashionerAdmin"
# admin.site.site_title="FashionerAdminPanel"