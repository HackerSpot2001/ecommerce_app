from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


""" Declaration of all routes comes under '/' """
urlpatterns = [
    path('', cache_page(60*60*2)(endpoints), name="All Endpoints"),
    # path('productpage', cache_page(60*60*2)(productpage), name="Product page"),
    # path('list_products', cache_page(60*60*2)(list_products), name="List Products"),
    path('productpage', productpage, name="Product page"),
    path('list_products', list_products, name="List Products"),
    path('get_product/<str:product>', get_product, name="Get Product"),
    path('create_product', view=create_product, name="Add Product"),
    path('update_product', view=update_product, name="Update Product"),
    path('delete_product', view=delete_product, name="Delete Product"),
]
