from shoppingcart.views import add_to_cart
from django.urls import path, include
from . import views

urlpatterns = [
    # Main url for shopping cart
    path('', views.view_shoppingcart, name="view_shoppingcart"),
    # Url for adding items to cart
    path('add/<item_id>/', views.add_to_cart, name="add_to_cart"),
    # Url for updating items in the cart
    path('update/<item_id>/', views.update_cart, name="update_cart"),
    # Url for removing items from the cart
    path('remove/<item_id>/', views.remove_item, name='remove_item'),
]
