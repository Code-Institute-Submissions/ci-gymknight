from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_onsave(sender, instance, created, **kwargs):
    ''' Update order total on creation of line item '''
    instance.order.update_total()
    
@receiver(post_delete, sender=OrderLineItem)
def update_onsave(sender, instance, **kwargs):
    ''' Update order total on deletion of line item '''
    instance.order.update_total()