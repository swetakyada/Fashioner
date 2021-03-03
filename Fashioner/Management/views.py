from django.shortcuts import render
from django.views.generic import ListView
from .models import Item, OrderItem, Order
# Create your views here.
def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product-page.html", context)

class HomeView(ListView):
    model=Item
    template_name="home-page.html"