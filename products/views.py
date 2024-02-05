from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Product, TextFeed, PhotoFeed
from django.contrib import messages
from .forms import NewItemForm, EditItemForm
<<<<<<< HEAD
from cart.models import CartItem, Cart
=======
>>>>>>> origin/master


# Create your views here.


def index(request):
    category = Category.objects.all()
    return render(request, "products/index.html", {
        "category": category,
    })


def explore(request):
    category = Category.objects.all()
    products = Product.objects.all()
    products_count = products.count()
    return render(request, "products/explore.html", {
        "category": category,
        "products": products,
        "products_count": products_count,
    })


def feed(request):
    text_feed = TextFeed.objects.all()
    photo_feed = PhotoFeed.objects.all()

    return render(request, "products/mans_grid.html", {
        "text_feed": text_feed,
        "photo_feed": photo_feed,
    })


def products_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    # category = Category.objects.get(id=category_pk)
    products = Product.objects.filter(category=category)
    product_count = products.count()

    return render(request, "products/explore.html", {
        "category": category,
        "products": products,
        "product_count": product_count,
    })


<<<<<<< HEAD
=======
# def new(request):
#     form = NewItemForm()
#
#     if request.method == "POST":
#         form = NewItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.created_by = request.user
#             product.save()
#             messages.success(request, "Product has been posted")
#
#             return redirect("products:explore")
#
#     return render(request, "products/form.html", {
#         "form": form,
#         "title": "Add item"
#     })
>>>>>>> origin/master

def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, "Your product has been successfully added")

            return redirect("products:explore")
    else:
        form = NewItemForm()

    return render(request, "products/form.html", {
        "form": form,
        "title": "Add item",
    })


def edit_item(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    form = EditItemForm(instance=item)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated")
            return redirect("products:detail", pk=pk)

    return render(request, "products/form.html", {
        "form": form,
        "title": "Edit Item"
    })


@login_required
<<<<<<< HEAD
=======
# def delete(request, pk):
#     product = get_object_or_404(Product, pk=pk, created_by=request.user)
#     if request.method == "POST":
#         product.delete()
#         messages.info(request, f"{product.title} has been deleted.")
#         return redirect("shop:index")
#
#     return render(request, "products/delete.html", {
#         "product": product,
#     })
>>>>>>> origin/master
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    if request.method == "POST":
        product.delete()
        messages.info(request, f"{product.name} has been deleted.")
        return redirect("products:index")

    return render(request, "products/delete.html", {
        "product": product,
    })


def shops(request):
    return render(request, "products/shops.html")


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_sold=False)
    related_items = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[:4]
    related_items2 = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)
    related_items_count = related_items2.count()
    return render(request, "products/detail.html", {
        "product": product,
        "related_items": related_items,
        "related_items_count": related_items_count,
        "related_items2": related_items2,
    })
