from django.db import models
from django.urls import reverse


class UrlRedirect(models.Model):
    """
    Classe que armazena as urls.

    Campos
    destino : guarda a url real
    slug: o apelido da url
    criado_em : momento que a url foi criada
    atualizado_em : momento que a url foi modifica
    """
    destino = models.URLField(max_length=1024)
    slug = models.SlugField(max_length=128, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.slug} -> {self.destino}'

    # Eu posso fazer isso ???
    def obtem_url_absoluta_para_url_reduzida(self):
        return reverse('redirecionar', kwargs={'slug': self.slug})

    def obtem_url_absoluta_para_o_relatorio(self):
        return reverse('relatorio', kwargs={'slug': self.slug})


class UrlLog(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    origem = models.URLField(max_length=1024, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(UrlRedirect, models.CASCADE, related_name='logs')

    def __str__(self):
        return 'log'
