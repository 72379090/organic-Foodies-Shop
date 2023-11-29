from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from .models import Product

from django.http import HttpResponse
from .credentials import *

def shop_grid(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, 'products/shop-grid.html', context)


def add_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfully')
            return redirect("add-products-url")
        else:
            messages.error(request, 'Product saving failed')
            return redirect("add-products-url")
    else:
        form = ProductForm()
    return render(request, 'products/add-products.html', {'form': form})


def latest_products(request):
    if request.method == "POST":
        form = LatestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfully')
            return redirect("latest-products-url")
        else:
            messages.error(request, 'Product saving failed')
            return redirect("latest-products-url")
    else:
        form = LatestForm()
    return render(request, 'products/latest_products.html', {'form': form})


def pay(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST['phone']
        amount = product.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "School fees"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse('Payment initiated Successfully to your devices')
    return render(request, 'products/pay.html', {'product': product})
