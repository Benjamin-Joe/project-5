"Views.py In Bag App"
from django.shortcuts import render


def view_bag(request):
    "Shopping bag view"
    return render(request, 'bag/bag.html')

