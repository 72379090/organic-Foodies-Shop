from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.shop_grid, name='shop-grid-url'),
    path('add-products/', my_views.add_products, name='add-products-url'),
    path('latest-products/', my_views.latest_products, name='latest-products-url'),
    path('pay/<id>', my_views.pay, name='pay-url'),

]
