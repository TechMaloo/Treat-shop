from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Product, TextFeed, PhotoFeed
from django.contrib import messages
from .forms import NewItemForm, EditItemForm


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


def products_by_category(request, category_pk):
    category = Category.objects.get(id=category_pk)  # id, Name, product
    products = Product.objects.filter(category=category)
    product_count = products.count()

    return render(request, "products/product_category.html", {
        "category": category,
        "products": products,
        "product_count": product_count,
    })


def new(request):
    form = NewItemForm()

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, "Product has been posted")

            return redirect("products:explore")

    return render(request, "products/form.html", {
        "form": form,
        "title": "Add item"
    })


def edit_item(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    form = EditItemForm(instance=item)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("products:detail", pk=pk)

    return render(request, "products/form.html", {
        "form": form,
        "title": "Edit Item"
    })


@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    if request.method == "POST":
        product.delete()
        messages.info(request, f"{product.title} has been deleted.")
        return redirect("shop:index")

    return render(request, "products/delete.html", {
        "product": product,
    })


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
