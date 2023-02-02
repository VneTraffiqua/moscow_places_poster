# Where to go - Moscow through the eyes of Artyom.

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
python3 manage.py migration
```

Start the development server

```
python3 manage.py runtime server
```

The site will be available at: http://127.0.0.1:8000

