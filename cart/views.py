from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product
from .forms import AddToCartForm


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

        messages.success(request, "Item added to cart")

    return redirect("cart:cart_detail")


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    messages.warning(request, "item removed from cart")
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    cart_count = Cart.objects.get(user=request.user)
    item_count = cart_count.items.count()
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {
        "cart": cart,
        "cart_count": cart_count,
        "item_count": item_count,
    })


def checkout(request):
    cart = Cart.objects.get(user=request.user)
    item_count = cart.items.count()
    return render(request, "cart/checkout.html", {
        "cart": cart,
        "item_count": item_count,
    })


def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.items.all().delete()
    messages.warning(request, "cart cleared")
    return redirect('cart:cart_detail')