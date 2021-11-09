from django.contrib import admin

from devpro.encurtador.models import UrlRedirect, UrlLog


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em')


@admin.register(UrlLog)
class UrlLog(admin.ModelAdmin):
    list_display = ('criado_em', 'criado_em', 'user_agent', 'host', 'ip', 'url_redirect')
