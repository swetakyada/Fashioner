from django.db import models


class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name= models.CharField(max_length=100)
    product_discription= models.CharField(max_length=300)
    price=models.DecimalField(max_digits=100000, decimal_places=2)
    product_image=models.ImageField(upload_to=None, height_field=300, width_field=300, max_length=500)