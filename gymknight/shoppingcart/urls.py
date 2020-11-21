from shoppingcart.views import add_to_cart
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_shoppingcart, name="view_shoppingcart"),
    path('add/<item_id>/', views.add_to_cart, name="add_to_cart"),
    path('update/<item_id>/', views.update_cart, name="update_cart"),
    path('remove/<item_id>/', views.remove_item, name='remove_item'),
]
