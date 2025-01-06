"""
URL configuration
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from ecommerce.store import views

router = routers.DefaultRouter()
router.register(r"artists", views.ArtistViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"files", views.DigitalFilesViewSet)
router.register(r"images", views.ImageViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"variations", views.VariationViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
