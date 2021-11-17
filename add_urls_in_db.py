import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devpro.settings')

django.setup()

from devpro.encurtador.models import UrlRedirect

urls = [
    {'destino': 'http://www.google.com', 'slug': 'google'},
    {'destino': 'http://pythonpro.com.br', 'slug': 'pythonpro'},
    {'destino': 'https://www.globo.com', 'slug': 'globo'},
    {'destino': 'https://github.com/HenriqueCCdA', 'slug': 'github'},
    {'destino': 'https://www.twitch.tv', 'slug': 'twitch'},
    {'destino': 'https://twitter.com', 'slug': 'twitter'},
    {'destino': 'https://stackoverflow.com', 'slug': 'stackoverflow'},
    {'destino': 'https://www.djangoproject.com/', 'slug': 'django'},
    {'destino': 'https://flask.palletsprojects.com/en/2.0.x/', 'slug': 'flask'},
]

for url in urls:
    destino = url['destino']
    slug = url['slug']
    url_db = UrlRedirect(destino=destino, slug=slug)
    url_db.save()
