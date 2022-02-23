"Urls.py In Home App"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
