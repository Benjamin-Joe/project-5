from django.shortcuts import render


def profile(request):
    "Displays user profiles"
    template = 'profiles/profile.html'
    context = {}
    return render(request, template, context)
