from django.http import JsonResponse
from django.shortcuts import render
from places import models
from django.shortcuts import get_object_or_404
from django.urls import reverse


def show_place_info(request, place_id):
    place = get_object_or_404(
        models.Place.objects.prefetch_related('photos'), id=place_id
    )
    place_info = {
        'title': place.title,
        'imgs': [photo.image.url for photo in place.photos.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }
    return JsonResponse(
        place_info, json_dumps_params={
            'ensure_ascii': False,
            'indent': 2,
        }
    )


def show_index(request):
    places = models.Place.objects.all()
    geo_json = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lon, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse('place_info', args=[place.id])
          }
        } for place in places
      ]
    }
    context = {
        'geo_json': geo_json,
    }

    return render(
        request, 'index.html', context=context
    )
