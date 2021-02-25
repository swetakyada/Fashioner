from django.db import models
from django.conf import settings

# Create your models here.
#Items class
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    headshot = models.ImageField(null=True, blank=True, upload_to="static/")
    category = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.title

# after adding to cart it will become OrderItem
class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    def __str__(self):
        return self.item.title

#Order object
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items= models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField( auto_now_add=True)
    Ordered_date = models.DateTimeField()
    def __str__(self):
        return self.user.username
