from django.contrib import admin

from devpro.encurtador.models.url import UrlRedirect, UrlLog


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em')


@admin.register(UrlLog)
class UrlLog(admin.ModelAdmin):
    list_display = ('origem', 'criado_em', 'user_agent', 'host', 'ip', 'url_redirect')

    def has_add_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False
