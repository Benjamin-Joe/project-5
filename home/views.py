"Views.py In Home App"
from django.shortcuts import render


def index(request):
    "Homepage view"
    return render(request, 'home/index.html')
