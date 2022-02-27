"Urls.py In Checkout App"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
