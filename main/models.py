from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    picture = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255)
    description = models.TextField()