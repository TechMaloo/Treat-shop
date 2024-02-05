from django.urls import path
from .views import add_to_cart, remove_from_cart, cart_detail, checkout, clear_cart

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('clear_cart/', clear_cart, name='clear_cart'),

    path('checkout/', checkout, name='checkout'),
]
