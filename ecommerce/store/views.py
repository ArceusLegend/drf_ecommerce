from rest_framework import permissions, viewsets

from ecommerce.store.models import Artist, Category, DigitalFiles, Image, Product, Variation
from ecommerce.store.serializers import (
    ArtistSerializer,
    CategorySerializer,
    DigitalFilesSerializer,
    ImageSerializer,
    ProductSerializer,
    VariationSerializer,
)


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `Artist` objects to be viewed or edited.
    """

    queryset = Artist.objects.all().order_by("-name")
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `Category` objects to be viewed or edited.
    """

    queryset = Category.objects.all().order_by("-name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class DigitalFilesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `DigitalFiles` objects to be viewed or edited.
    """

    queryset = DigitalFiles.objects.all().order_by("-file")
    serializer_class = DigitalFilesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `Image` objects to be viewed or edited.
    """

    queryset = Image.objects.all().order_by("-name")
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `Product` objects to be viewed or edited.
    """

    queryset = Product.objects.all().order_by("-published_date")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class VariationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `Variation` objects to be viewed or edited.
    """

    queryset = Variation.objects.all().order_by("-name")
    serializer_class = VariationSerializer
    permission_classes = [permissions.IsAuthenticated]
