from django.shortcuts import render
from django.db.models import Q

from products.models import Product


def search(request):
    query = request.GET.get("query", "")
    products = Product.objects.filter(is_sold=False)

    if query:
        products = products.filter(Q(name__icontains=query) | Q(category__icontains=query))

    return render(request, "search/find.html", {
        "products": products,
        "query": query,
    })
