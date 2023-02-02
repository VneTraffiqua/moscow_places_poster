from django.contrib import admin
from .models import Place, Photo
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class PhotosInline(SortableStackedInline):
    model = Photo
    readonly_fields = ['show_image', ]

    def show_image(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" height=200 />'
        )


admin.site.register(Photo)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = [
        'title', 'description_short'
    ]

    inlines = [PhotosInline]



