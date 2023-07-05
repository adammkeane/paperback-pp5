from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from books.models import Book
# from profiles.models import UserProfile
# from profiles.forms import UserProfileForm
from bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        # following 2 are temp
        'stripe_public_key': 'pk_test_51N6zmeHzXh3qSJQeqf3A0GMXR1uv1qMO3h0OuodCwCZ7Iq5IKvPGIW6gXwWMNzW7ld6kGMMVy7FdPiJViDM7cPbo00Ugf38Z1E',
        'client_secret': 'test client secret',
        # 'stripe_public_key': stripe_public_key,
        # 'client_secret': intent.client_secret,
    }

    return render(request, template, context)
