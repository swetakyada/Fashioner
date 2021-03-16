from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
import random
import string

CATAGORY_CHOISES = {
    ('M','Men'),
    ('W','Women'),
    ('G','Girls'),
    ('B','Boys'),
}

SIZE_CHOISES = { 
    ('28','S'),
    ('30','M'),
    ('32','L'),
    ('34','XL'),
    ('36','XXL'),
    ('38','XXXL'),
 }

# def custom_id(cname, cfor):
#     return ' '.join(map(str,[cfor, cname]))

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_for = models.CharField(choices=CATAGORY_CHOISES, max_length=5)
    category_id = models.CharField(primary_key=True, default = " ", max_length=100)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    image1 = models.CharField(max_length = 1000, default="")
    image2 = models.CharField(max_length = 1000, default="")
    image3 = models.CharField(max_length = 1000, default="")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default="")
    description = models.CharField(max_length = 1000, default="")
    sizes = MultiSelectField(choices = SIZE_CHOISES, default="")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1) 
    size = models.CharField(choices=SIZE_CHOISES, max_length=3, default="")
    price = models.IntegerField(default=0)

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Cart)
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField(default=0)