import uuid

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Product Category table implimented with MPTT
    """

    uuid: models.UUIDField = models.UUIDField(
        default=uuid.uuid4, primary_key=True, blank=False, null=False, editable=False
    )
    name: models.CharField = models.CharField(
        max_length=100, null=False, unique=False, blank=False, verbose_name=_("Category name")
    )
    slug: models.SlugField = models.SlugField(
        max_length=150, null=False, unique=False, blank=False, verbose_name=_("URL-safe category name")
    )
    is_active: models.BooleanField = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Parent Category"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self):
        return self.name


class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, blank=False, editable=False)
    image = models.ImageField(upload_to="audiobooks/images/", blank=True, null=True)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(blank=True)
    alt_text = models.CharField(max_length=125, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product image")
        verbose_name_plural = _("Product images")


class Artist(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False, editable=False)
    name = models.CharField(max_length=255)
    artist_image = models.ImageField(upload_to="artists/pfp/", blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class DigitalFiles(models.Model):
    file = models.FileField()

    class Meta:
        verbose_name_plural = _("Digital Files")


class Product(models.Model):
    category = TreeManyToManyField(Category)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="product_creator"
    )
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False, editable=False)
    sku = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    artist = models.ManyToManyField(Artist, related_name="products", blank=True)  # type: ignore
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    product_image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, editable=True)
    sale_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, null=True, blank=True)
    is_digital = models.BooleanField(null=False, blank=False)
    associated_files = models.ManyToManyField(DigitalFiles, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def validate_digital_has_file(self):
        if self.is_digital and (not self.associated_files):
            raise ImproperlyConfigured(f"Product {self.title} is digital, but no downloadable files detected")


class Variation(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False, editable=False)
    for_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price_increase = models.DecimalField(max_digits=4, decimal_places=2)
    is_downloadable = models.BooleanField(default=False)
    downloadable_file = models.FileField(upload_to="audiobooks/downloadable/", blank=True, null=True)
    variation_image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

    def validate_downloadable_includes_file(self):
        if self.is_downloadable and (not self.downloadable_file.url):
            raise ImproperlyConfigured(f"File '{self.name}' is downloadable, but no URL was provided")
