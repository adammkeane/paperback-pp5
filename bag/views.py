from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from books.models import Book
from django.conf import settings


def view_bag(request):
    """ View that renders page with shopping bag contents """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of selected item to shopping bag """

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    option = None
    # wh_secret = settings.STRIPE_WH_SECRET
    # print(wh_secret)
    if 'book_option' in request.POST:
        option = request.POST['book_option']

    bag = request.session.get('bag', {})

    if option:
        if item_id in list(bag.keys()):
            if option in bag[item_id]['items_by_option'].keys():
                bag[item_id]['items_by_option'][option] += quantity
    #             messages.success(
    #                 request, f'Updated option {option.upper()} {book.name} quantity to {bag[item_id]["items_by_option"][option]}')
            else:
                bag[item_id]['items_by_option'][option] = quantity
    #             messages.success(
    #                 request, f'Added option {option.upper()} {book.name} to your bag')
        else:
            bag[item_id] = {'items_by_option': {option: quantity}}
    #         messages.success(
    #             request, f'Added option {option.upper()} {book.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
    #         messages.success(
    #             request, f'Updated {book.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {book.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified bookto the specified amount"""

    # book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    option = None
    if 'book_option' in request.POST:
        option = request.POST['book_option']
    bag = request.session.get('bag', {})

    if option:
        if quantity > 0:
            bag[item_id]['items_by_option'][option] = quantity
            # messages.success(
            #     request, f'Updated option {option.upper()} {book.name} quantity to {bag[item_id]["items_by_option"][option]}')
        else:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_option']:
                bag.pop(item_id)
            # messages.success(
            #     request, f'Removed option {option.upper()} {book.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            # messages.success(
            #     request, f'Updated {book.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            # messages.success(request, f'Removed {book.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        # book = get_object_or_404(Book, pk=item_id)
        option = None
        if 'book_option' in request.POST:
            option = request.POST['book_option']
        bag = request.session.get('bag', {})

        if option:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_option']:
                bag.pop(item_id)
            # messages.success(
            #     request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            # messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
