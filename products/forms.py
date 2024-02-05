from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import Product, Category, PhotoFeed, TextFeed


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name", "price", "description", "image")


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name", "price", "description", "image")


# class UploadFeedForm(forms.ModelForm):
#     class Meta:
#         model = T
#         fields = ("caption", "image", "text")
#
#
# class EditFeedForm(forms.ModelForm):
#     class Meta:
#         model = Feed
#         fields = ("caption", "image", "text")

