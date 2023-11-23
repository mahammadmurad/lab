from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_name', 'price', 'stock' )
    prepopulated_fields = {'slug': ('product_name',)}


# Register your models here.
