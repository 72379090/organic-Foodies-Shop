from django.shortcuts import render
from products.models import latest_products


def home(request):
    all_latest_products = latest_products.objects.all()
    context = {"latest_products": all_latest_products}
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def shop_details(request):
    return render(request, 'shop-details.html')


def shoping_cart(request):
    return render(request, 'shoping-cart.html')
