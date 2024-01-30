from django.contrib import admin
from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("explore/", views.explore, name="explore"),
    path("shops/", views.shops, name="shops"),
    path("feed/", views.feed, name="feed"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("new/", views.new, name="new"),
    # path("delete/<>/", views.delete, name="delete"),
    # path("delete/<int:pk>/", views.delete, name="delete"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("category/<int:category_pk>/", views.products_by_category, name="product_category"),
    path("product-category/<int:pk>/", views.products_by_category, name="products_by_category"),
]
