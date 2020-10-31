from django.contrib import admin
from .models import Product, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
        'category'
    )
    
    ordering = ('sku', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
