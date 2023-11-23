from django.db import models
from category.models import *

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    desc = models.TextField(blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='product')
    stock = models.IntegerField()
    is_avialable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
# Create your models here.
