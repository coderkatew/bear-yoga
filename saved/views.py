from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product


def view_saved(request):
    """ A view to show products that have been saved by user """

    return render(request, 'saved/saved.html')


def product_detail(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def adjust_saved(request, item_id):
    """ Adjust quantity """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    saved = request.session.get('saved', {})

    if quantity > 0:
        saved[item_id] = quantity
        messages.success(request, f'Updated quantity of {product.name} to {saved[item_id]}.')
    else:
        saved.pop(item_id)
        messages.success(request, f'{product.name} has been removed.')

    request.session['saved'] = saved
    return redirect(reverse('view_saved'))


def add_to_saved(request, item_id):
    """ A view to add a product to Saved For Later """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    saved = request.session.get('saved', {})

    if item_id in list(saved.keys()):
        saved[item_id] += quantity
        messages.success(request, f'Updated quantity of {product.name} to {saved[item_id]}.')
    else:
        saved[item_id] = quantity
        messages.success(request, f'{product.name} has been added to Saved For Later.')

    request.session['saved'] = saved

    return redirect(redirect_url)


def remove_from_saved(request, item_id):
    """ Remove product from Saved For Later """

    try:

        saved = request.session.get('saved', {})
        product = get_object_or_404(Product, pk=item_id)

        saved.pop(item_id)
        messages.success(request, f'{product.name} has been removed from Saved For Later.')

        request.session['saved'] = saved
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=200)
