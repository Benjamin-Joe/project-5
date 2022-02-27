"Views File In Checkout App"
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    "View for the checkout menu"
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Nothing In Basket')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JhgJpKGApoDuOAh8jmkNakFGFYSc75EyTwrsQt2Nj1xLKgtkfbDXPvKFUJs848ovL1P8CoxP12beexihc0K2zka00Nb2w8P9Y',
        'client_secret': 'testingclientsecret',

    }
    return render(request, template, context)
