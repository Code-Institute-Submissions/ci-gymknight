from django.db import models

# Create your models here.

class Category(models.Model):
    '''Databse model for the categories'''

    # Override default category plural
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=256)
    friendly_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    def return_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    '''Database model for the products'''
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
