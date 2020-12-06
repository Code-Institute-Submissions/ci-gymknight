import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from django_countries.fields import CountryField

# Create your models here.

class Order(models.Model):
    '''class defining order details'''
    order_no = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country*", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city_or_town = models.CharField(max_length=40, null=False, blank=False)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    
    def _generate_order_number(self):
        '''Private method used to generate random order number'''
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        ''' override default save function'''
        if not self.order_no:
            self.order_no = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def update_total(self):
        '''update total everytime an individual product is added'''
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total_sum']
        if self.order_total < settings.FREE_DELIVERY_MINIMUM:
            self.delivery_cost = settings.STD_DELIVERY_CHARGE
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
        
    def __str__(self):
        return self.order_no


class OrderLineItem(models.Model):
    '''order class for item by item, size by size'''
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=3, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    
    def save(self, *args, **kwargs):
        ''' override default save function'''
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_no}'