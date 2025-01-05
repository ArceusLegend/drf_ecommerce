from django.contrib import admin

from ecommerce.store.models import Artist, Category, DigitalFiles, Image, Product, Variation

# Register your models here.
admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(DigitalFiles)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Variation)
