from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=False, unique=True)
    phone_no = models.CharField(max_length=15, unique=True)