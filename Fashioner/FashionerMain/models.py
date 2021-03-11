from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

CATAGORY_CHOISES={
    ('M','Men'),
    ('W','Women'),
    ('K','Kids'),
}

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_for = models.CharField(choices=CATAGORY_CHOISES, max_length=5)

    def custom_id(self, cname, cfor):
        return ' '.join(map(str,[cfor, cname]))

    category_id = models.CharField(primary_key=True, default = custom_id(None, category_name, category_for), max_length=50)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image1 = models.CharField(max_length = 500, default="")
    image2 = models.CharField(max_length = 500, default="")
    image3 = models.CharField(max_length = 500, default="")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default="")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1) 

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Cart)
    ordered_date = models.DateTimeField(auto_now_add=True)