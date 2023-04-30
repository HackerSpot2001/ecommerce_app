from django.urls import path
from .views import *
urlpatterns = [
    path('',view=endpoints,name="All Endpoints"),
    path('productpage',view=productpage,name="Product page"),
    path('get_product/<str:product>',view=get_product,name="Get Product"),
    path('list_products',view=list_products,name="List Products"),
    path('create_product',view=create_product,name="Add Product"),
    path('update_product',view=update_product,name="Update Product"),
    path('delete_product',view=delete_product,name="Delete Product"),
]
