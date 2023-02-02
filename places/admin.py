from django.contrib import admin
from .models import Place, Photo


class PhotosInline(admin.TabularInline):
    model = Photo


admin.site.register(Photo)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'description_short'
    ]
    inlines = [PhotosInline]
