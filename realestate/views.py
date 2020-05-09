from django.shortcuts import render, get_object_or_404
from .models import Listing, ListingImage


def home(request):
    listings = Listing.objects.all()
    return render(request, 'index.html',
                  {'listings': listings})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


def subscribe(request):
    return render(request, 'subscribe.html')


def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listing.html',
                  {'listings': listings}, )


def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    photos = ListingImage.objects.filter(listing=listing)
    return render(request, 'details.html', {
        'listing': listing,
        'photos': photos
    })
