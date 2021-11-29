from django.shortcuts import render
from .models import Team
from listings.models import Listing
from listings.choices import price_choice, bedroom_choice, state_choice

# Create your views here.
def home(request):
    latest_listings = Listing.objects.order_by('-list_date')[:3]
    
    data = {
        'latest_listings' : latest_listings,
        'price_choice' : price_choice,
        'bedroom_choice' : bedroom_choice,
        'state_choice' : state_choice,
    }
    return render(request, 'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    seller_of_month = Team.objects.order_by().filter(is_mvp = True)

    data = {
        'teams':teams,
        'seller_of_month':seller_of_month,
    }
    return render(request, 'pages/about.html',data)

