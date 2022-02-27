from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import OrderLineItem

def update_on_save()