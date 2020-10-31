from django.urls import path, include
from . import views

urlpatterns = [
    path('/bag', views.view_shoppingbag, name="view_shoppingbag")
]
