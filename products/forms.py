from django import forms
from .models import Product, latest_products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'qtty', 'price', 'desc', 'image']


class LatestForm(forms.ModelForm):
    class Meta:
        model = latest_products
        fields = ['name', 'size', 'price', 'desc', 'image']
