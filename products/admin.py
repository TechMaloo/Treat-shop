from django.contrib import admin


from .models import Product, Category, TextFeed, PhotoFeed
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(TextFeed)
admin.site.register(PhotoFeed)


