from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 50)
    #category_for = models.Choices()
    #products = models.ExpressionList()