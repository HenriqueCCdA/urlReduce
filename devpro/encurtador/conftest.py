from typing import List, Tuple
import pytest
from model_bakery import baker
from devpro.encurtador.models import UrlRedirect, UrlLog


@pytest.fixture
def url_encurtada(db) -> UrlRedirect:
    '''
    Gera as url1.

    return: retorna a url1
    '''
    return baker.make(UrlRedirect)


@pytest.fixture
def lista_urls(db) -> List[UrlRedirect]:
    '''
    Gera as url1 e url2.

    return: retorna um lista com as urls
    '''
    return baker.make(UrlRedirect, 2)


@pytest.fixture
def logs(lista_urls) -> Tuple[UrlLog]:
    '''
    Gera 3 logs para url1 e 8 logs para url2.

    return: retorna a tupla (url1, url2)
    '''
    log_url1 = baker.make(UrlLog, 3, url_redirect=lista_urls[0])
    log_url2 = baker.make(UrlLog, 8, url_redirect=lista_urls[1])
    return log_url1, log_url2
