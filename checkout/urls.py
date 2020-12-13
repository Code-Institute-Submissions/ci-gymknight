from django.urls import path, include
from . import views
from .webhooks import webhook

#  Home url pattern
urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('successful_checkout/<order_no>', views.successful_checkout, name='successful_checkout'),
    path('wh/', webhook, name='webhook')
]
