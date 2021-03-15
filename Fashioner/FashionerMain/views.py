from django.shortcuts import render
from django.views.generic import ListView
from .models import Product,Cart,Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/')
def products(request):
    products = Product.objects.all()
    men = Category.objects.filter(category_for="M")
    women = Category.objects.filter(category_for="W")
    girls = Category.objects.filter(category_for="G")
    boys = Category.objects.filter(category_for="B")
    context = {
        'items': products,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "home-page.html", context)

# class HomeView(ListView):
#     model=Item
#     template_name="home-page.html"
@login_required(login_url='/accounts/')
def product_page(request, pid):
    product = Product.objects.get(id=pid)
    men = Category.objects.filter(category_for="M")
    women = Category.objects.filter(category_for="W")
    girls = Category.objects.filter(category_for="G")
    boys = Category.objects.filter(category_for="B")
    context = {
        'product': product,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "product-page.html", context)

def category_page(request, cid):
    products = Product.objects.filter(category_id = cid)
    men = Category.objects.filter(category_for="M")
    women = Category.objects.filter(category_for="W")
    girls = Category.objects.filter(category_for="G")
    boys = Category.objects.filter(category_for="B")
    context = {
        'products': products,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "category-page.html", context)
