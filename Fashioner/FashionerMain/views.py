from django.shortcuts import render
from django.views.generic import ListView
from .models import Product,Cart
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/')
def products(request):
    products = Product.objects.all()
    context = {
        'items': products,
    }
    return render(request, "home-page.html", context)

# class HomeView(ListView):
#     model=Item
#     template_name="home-page.html"
@login_required(login_url='/accounts/')
def product_page(request, pid):
    product = Product.objects.get(id=pid)
    return render(request, "product-page.html", {'product': product})
