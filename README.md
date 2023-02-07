# Where to go - Moscow through the eyes of Artyom.

### [https://vnetraffiqua.pythonanywhere.com/](https://vnetraffiqua.pythonanywhere.com/)

Site about the most interesting places in Moscow. Artyom's author's project.
 
![site.png](static%2F.gitbook%2Fassets%2Fsite.png)

## Environment variables

Part of the project settings is taken from the environment variables. To define them, create a `.env` file next to `manage.py` and write data there in the following format: `VARIABLE=value`.

There are 3 variables available:
- `DEBUG` - debug mode. Set to `True` to see debug information in case of an error.
- `SECRET_KEY` — project secret key
-  `STATIC_URL` - path to static files

## Launch

You will need Python 3 to run the site.

Download the code from GitHub. Install dependencies:

```
pip install -r requirements.txt
```

Create a SQLite database

```
python3 manage.py migrate
```

Start the development server

```
python3 manage.py runserver
```

The site will be available at: http://127.0.0.1:8000

## Load place from json

You can load location from json file:

```commandline
python manage.py load_place <json-url>
```

#### json-file example:

```commandline
{
    "title": "Эйфелева башня в Москве",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/8868d171420b5221f8f50af5e95a7b12.jpeg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/46cb25cf1719bf546c8bbcf1b51ba4f4.jpeg"
    ],
    "description_short": "Вы можете поехать в Париж и отстоять огромную очередь, 
    чтобы посетить главную его достопримечательность — великолепную Эйфелеву башню.
    А можете просто сесть в метро и, не выезжая за пределы МКАД, прикоснуться к точной 
    её копии.",
    "description_long": "<p><strong>Эйфелева башня в Москве</strong> находится 
    недалеко от станции метро «Авиамоторная» на территории одного из производственных
    предприятий — завода «Москабельмет». Соорудили точную копию мировой архитектурной 
    знаменитости сами рабочие этого завода. Высота заводской башни — 15 метров (для 
    справки — высота оригинальной, парижской Эйфелевой башни составляет 324 метра)."
    "coordinates": {
        "lng": "37.71241599999999",
        "lat": "55.74669399999998"
    }
}
```
