"Views.py In Bag App"
from django.shortcuts import HttpResponse, get_object_or_404, render, reverse, redirect
from django.contrib import messages
from products.models import Product


def add_to_bag(request, item_id):
    "Adding multiple items to shopping bag"

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        messages.success(request, f'Added {product.title} to your bag')
        bag[item_id] += quantity

    else:
        messages.success(request, f'Added {product.title} to your bag')
        bag[item_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    "Adjusting items in shopping bag"
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        del bag[item_id]
        bag.pop(item_id)
    return redirect(reverse('view_bag'))


def view_bag(request):
    "Shopping bag view"
    return render(request, 'bag/bag.html')


def remove_from_bag(request, item_id):
    "Removing items from shopping bag"
    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.title} to your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Something Went Wrong With:  (e)')
        return HttpResponse(status=500)
