from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    picture = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    allow_range = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255)
    description = models.TextField()
    
# class Seller(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField(blank=True, null=True)
#     description = models.TextField()
