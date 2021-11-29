from django.contrib import admin
from django.utils.html import format_html
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo_main.url))

    thumbnail.short_description = 'Photo'
    
    list_display = ('id','title','thumbnail','state','team','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','state')
    list_editable = ('is_published',)

admin.site.register(Listing, ListingAdmin)