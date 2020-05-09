from django.db import models

# Create your models here.


class ListingImage(models.Model):
    listing = models.ForeignKey('Listing', default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listing/listpics/')

    def __str__(self):
        return self.listing.title


class Listing(models.Model):
    property_title = models.CharField(max_length=100)
    PROPERTY_STATUS_CHOICES = [
        ('For Rent', 'For Rent'),
        ('For Sale', 'For Sale'),
        ('For Lease', 'For Lease')
    ]
    property_status = models.CharField(
        max_length=20,
        choices=PROPERTY_STATUS_CHOICES,
        default='FR'
    )
    PROPERTY_TYPE_CHOICES = [
        ('Bungalo', 'Bungalo'),
        ('Office', 'Office'),
        ('Duplex', 'Duplex'),
        ('Store', 'Store'),
        ('Land', 'land'),
    ]
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default='BG'
    )
    price = models.IntegerField()
    property_area = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    image = models.ImageField(blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    description = models.TextField()
    date = models.TimeField()

    def __str__(self):
        return self.title


