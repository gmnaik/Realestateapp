from django.core import paginator
from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choice, bedroom_choice, state_choice

# Create your views here.
def listings(request):
    all_listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(all_listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    data = {
        'all_listings' : paged_listings,
    }
    return render(request, 'listings/listings.html', data)

def listing_detail(request, id):
    single_listing = get_object_or_404(Listing,pk=id)
    data = {
        'single_listing': single_listing,
    }
    return render(request, 'listings/listing_detail.html',data)

def search(request):
    all_listings = Listing.objects.order_by('-list_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            all_listings = all_listings.filter(description__icontains = keyword)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            all_listings = all_listings.filter(city__iexact = city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            all_listings = all_listings.filter(state__iexact = state)
    
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            all_listings = all_listings.filter(bedrooms__iexact = bedrooms)
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            all_listings = all_listings.filter(price__lte = price)


    data = {
        'all_listings' : all_listings,
        'price_choice' : price_choice,
        'bedroom_choice' : bedroom_choice,
        'state_choice' : state_choice,
    }
    return render(request, 'listings/search.html', data)
    