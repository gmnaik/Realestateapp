from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id','name','thumbnail','email','is_mvp')
    list_display_links = ('id','name')
    search_fields = ('name','email')
    list_editable = ('is_mvp',)

admin.site.register(Team, TeamAdmin)