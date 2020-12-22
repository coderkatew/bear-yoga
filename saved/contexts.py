from django.shortcuts import get_object_or_404
from products.models import Product


def saved_contents(request):

    saved_items = []
    total = 0
    product_count = 0
    saved = request.session.get('saved', {})


    for item_id, item_data in saved.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        saved_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    context = {
        'saved_items': saved_items,
        'total': total,
        'product_count': product_count,
    }
    return context
