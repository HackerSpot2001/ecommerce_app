from django.contrib import admin
from django.urls import path, include


""" Declaration of routes '/' and '/admin' """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]
