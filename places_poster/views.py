from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.shortcuts import render
from places import models
from django.shortcuts import get_object_or_404
import json


def get_place_info(place):
    details_url = {
        'title': place.title,
        'imgs': place.photos,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lon, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": {}
        }
    }


def get_details_url(place):
    return {
        'title': place.title,
        'imgs': 'place.photos',
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }


def show_place_info(request, place_id):
    place = get_object_or_404(models.Place, id=place_id)
    place_info = {
        'title': place.title,
        'imgs': [photo.image.url for photo in place.photos.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
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
    moscow_legends = models.Place.objects.get(title='Экскурсионная компания «Легенды Москвы»')
    roofs24 = models.Place.objects.get(title='Экскурсионный проект «Крыши24.рф»')

    geo_json = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [moscow_legends.lon, moscow_legends.lat]
          },
          "properties": {
            "title": moscow_legends.title,
            "placeId": "moscow_legends",
            "detailsUrl": "./static/places/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [roofs24.lon, roofs24.lat]
          },
          "properties": {
            "title": roofs24.title,
            "placeId": "roofs24",
            "detailsUrl": "./static/places/roofs24.json"
          }
        }
      ]
    }
    context = {
        'geo_json': geo_json,
    }

    return render(
        request, 'index.html', context=context
    )
