from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'buyer', 'category', 'condition', 'description']
    list_filter = ['created', 'category']