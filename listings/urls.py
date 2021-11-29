from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:id>', views.listing_detail, name='listing_detail'),
    path('search', views.search, name='search'),
]
