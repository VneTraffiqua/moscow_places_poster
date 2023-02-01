from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from places import models
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
            "detailsUrl": json.loads(details_url)
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


def show_index(request):
    # features_list = [
    #     get_details_url(place) for place in models.Place.objects.all()
    # ]
    #
    # places_geo = {
    #   "type": "FeatureCollection",
    #   "features": features_list
    # }
    context = {'geo_json': {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "./static/places/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "./static/places/roofs24.json"
          }
        }
      ]
    }
    }

    return render(
        request, 'index.html', context=context
    )
