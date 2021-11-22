import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devpro.settings')

django.setup()

from devpro.encurtador.models import UrlRedirect

urls = (
    {'destino': 'http://www.google.com', 'slug': 'google'},
    {'destino': 'http://pythonpro.com.br', 'slug': 'pythonpro'},
    {'destino': 'https://www.globo.com', 'slug': 'globo'},
    {'destino': 'https://github.com/HenriqueCCdA', 'slug': 'github'},
    {'destino': 'https://www.twitch.tv', 'slug': 'twitch'},
    {'destino': 'https://twitter.com', 'slug': 'twitter'},
    {'destino': 'https://stackoverflow.com', 'slug': 'stackoverflow'},
    {'destino': 'https://www.djangoproject.com/', 'slug': 'django'},
    {'destino': 'https://flask.palletsprojects.com/en/2.0.x/', 'slug': 'flask'},
    {'destino': 'http://www.google.com', 'slug': 'google2'},
    {'destino': 'http://pythonpro.com.br', 'slug': 'pythonpro2'},
    {'destino': 'https://www.globo.com', 'slug': 'globo2'},
    {'destino': 'https://github.com/HenriqueCCdA', 'slug': 'github2'},
    {'destino': 'https://www.twitch.tv', 'slug': 'twitch2'},
    {'destino': 'https://twitter.com', 'slug': 'twitter2'},
    {'destino': 'https://stackoverflow.com', 'slug': 'stackoverflow2'},
    {'destino': 'https://www.djangoproject.com/', 'slug': 'django2'},
    {'destino': 'https://flask.palletsprojects.com/en/2.0.x/', 'slug': 'flask2'},
    {'destino': 'http://www.google.com', 'slug': 'google3'},
    {'destino': 'http://pythonpro.com.br', 'slug': 'pythonpro3'},
    {'destino': 'https://www.globo.com', 'slug': 'globo3'},
    {'destino': 'https://github.com/HenriqueCCdA', 'slug': 'github3'},
    {'destino': 'https://www.twitch.tv', 'slug': 'twitch3'},
    {'destino': 'https://twitter.com', 'slug': 'twitter3'},
    {'destino': 'https://stackoverflow.com', 'slug': 'stackoverflow3'},
    {'destino': 'https://www.djangoproject.com/', 'slug': 'django3'},
    {'destino': 'https://flask.palletsprojects.com/en/2.0.x/', 'slug': 'flask3'},
)

for url in urls:
    destino = url['destino']
    slug = url['slug']
    url_db = UrlRedirect(destino=destino, slug=slug)
    url_db.save()
