from django.contrib import admin

from .models import Album,Artist

class AlbumAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Album._meta.fields]
    
class ArtistAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Artist._meta.fields]
    

admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
