from django.contrib import admin
from .models import Listing, ListingImage


class ListingImageAdmin(admin.StackedInline):
    model = ListingImage


class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageAdmin]
    list_display = ('property_title', 'property_status', 'property_type', 'price',
                    'property_area', 'bedrooms', 'bathrooms', 'image', 'address', 'city',
                    'state', 'zip_code', 'description')

    class Meta:
        model = Listing


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Listing, ListingAdmin)