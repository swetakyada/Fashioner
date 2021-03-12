from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.
def products(request):
    context = {
        'items': Product.objects.all()
    }
    return render(request, "home-page.html", context)

# class HomeView(ListView):
#     model=Item
#     template_name="home-page.html"

