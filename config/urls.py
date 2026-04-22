from django.contrib import admin
from django.urls import path

from shop.api import api
from shop.views import home, products_partial

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("partials/products/", products_partial),
    path("api/", api.urls),
]
