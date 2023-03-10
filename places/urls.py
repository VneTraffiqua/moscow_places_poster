from django.urls import path, include
from places import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.show_index),
    path('places/<int:place_id>', views.show_place_info, name='place_info'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
