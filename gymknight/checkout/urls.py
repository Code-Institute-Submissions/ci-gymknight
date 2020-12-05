from django.urls import path, include
from . import views

#  Home url pattern
urlpatterns = [
    path('', views.checkout, name="checkout")
]
