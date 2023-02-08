from django.core.management.base import BaseCommand
import requests
from places.models import Place, Photo
from io import BytesIO
import os


class Command(BaseCommand):
    help = 'Loads place from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            type=str,
            help='URL of the JSON file to load'
        )

    def handle(self, *args, **options):
        response = requests.get(options['json_url'])
        response.raise_for_status()
        place_info = response.json()
        place, created = Place.objects.update_or_create(
            title=place_info['title'],
            defaults={
                'title': place_info['title'],
                'short_description': place_info['description_short'],
                'long_description': place_info['description_long'],
                'lat': place_info['coordinates']['lat'],
                'lon': place_info['coordinates']['lng']
            }

        )
        if place_info['imgs']:
            place.photos.clear()
            for num, url in enumerate(place_info['imgs']):
                response = requests.get(url)
                response.raise_for_status()
                byte_image = BytesIO(response.content)
                image_name = os.path.basename(url)
                place_image, created = place.photos.get_or_create(
                    number=num,
                    place=place.title
                )
                place_image.image.save(image_name, byte_image, save=True)
        [print('Place created') if created else print("Place updated")]
        Photo.objects.filter(place=None).delete()

