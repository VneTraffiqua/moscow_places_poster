from django.contrib import admin
from .models import Place, Photo
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class PhotosInline(SortableStackedInline):
    model = Photo
    readonly_fields = ['show_image', ]
    extra = 0

    def show_image(self, obj):
        return format_html(
            '<img src="{}" max-height=200 width=200/>', obj.image.url
        )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'short_description']
    inlines = [PhotosInline]
