from rest_framework import serializers

from ecommerce.store.models import Artist, Category, DigitalFiles, Image, Product, Variation


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DigitalFilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DigitalFiles
        fields = "__all__"


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class VariationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variation
        fields = "__all__"
