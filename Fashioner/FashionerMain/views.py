from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Product,Cart,Category,Order,WishList
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User


# Create your views here.


men = Category.objects.filter(category_for="M")
women = Category.objects.filter(category_for="W")
girls = Category.objects.filter(category_for="G")
boys = Category.objects.filter(category_for="B")


@login_required(login_url='/accounts/')
def products(request):
    products = Product.objects.all()
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
def product_page(request):
    id = int(request.POST['pid'])-1
    product = Product.objects.get(id = str(id))
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
    
@login_required(login_url='/accounts/')
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

def user_cart(request):
    user = request.user
    items = Cart.objects.filter(user = user)
    length = len(items)
    total = 0 
    for item in items:
        if(item.ordered == False):
            total = total + item.price
    context = {
        'items': items, 
        'length': length, 
        'total': total,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "cart-page.html", context)

def add_to_cart(request):
    user = request.user
    itm = Product.objects.get(id=request.POST.get('pid'))
    item = Cart(user = user, product = itm, quantity = request.POST.get('qty'), size = request.POST.get('size'))
    item.price = int(itm.price) * int(item.quantity)
    item.save()
    return redirect(user_cart)

def remove_from_cart(request):
    cid = request.POST.get('cid')
    cart_item = Cart.objects.get(id = cid)
    cart_item.delete()
    return redirect(user_cart)

def update_cart_item(request):
    ciid = request.POST.get('ciid')
    cart_item = Cart.objects.get(id = ciid)
    cart_item.size = request.POST.get('size')
    cart_item.quantity = request.POST.get('qty')
    cart_item.price = int(cart_item.quantity) * int(cart_item.product.price)
    cart_item.save()
    return redirect(user_cart)

def place_order(request):
    user = request.user
    items = Cart.objects.filter(user = user)
    length = len(items)
    total = 0 
    for item in items:
        total = total + item.price
    order = Order(user = user, total_amount = total, address = request.POST.get('address'), address2 = request.POST.get('address2'), country = request.POST.get('country'), state = request.POST.get('state'), pincode = request.POST.get('pincode'))
    order.save()
    for item in items:
        order.products.add(item)
        item.ordered = True
    order.save()
    return redirect(profile_page)

def checkout(request):
    user = request.user
    items = Cart.objects.filter(user = user)
    length = len(items)
    total = 0 
    for item in items:
        if(item.ordered == False):
            total = total + item.price
    context = {
        'user': user,
        'items': items, 
        'length': length, 
        'total': total,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "checkout-page.html", context)

def user_wishlist(request):
    user = request.user
    items = WishList.objects.filter(user = user)
    length = len(items)
    context = {
        'items': items,
        'length': length,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "wishlist-page.html", context)

def add_to_wishlist(request):
    user = request.user
    product = Product.objects.get(id=request.POST.get('pid'))
    item = WishList(user = user, product = product)
    item.save()
    return redirect(user_wishlist)

def remove_from_wishlist(request):
    wid = request.POST.get('wid')
    wishlist_item = WishList.objects.get(id = wid)
    wishlist_item.delete()
    return redirect(user_wishlist)

def profile_page(request):
    orders = Order.objects.filter(user = request.user)
    context = {
        'orders': orders,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "profile.html", context)
