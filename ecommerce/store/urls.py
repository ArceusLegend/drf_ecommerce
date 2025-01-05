from django.urls import path

from ecommerce.store.views import main

urlpatterns = [path("", main)]
