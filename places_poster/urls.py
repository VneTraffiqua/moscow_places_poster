from django.contrib import admin
from django.urls import path
from places_poster import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index)
]
