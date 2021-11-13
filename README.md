# 🐍 urlReduce 🐍

![](https://img.shields.io/github/last-commit/HenriqueCCdA/urlReduce?style=plasti&ccolor=blue)
![](https://img.shields.io/badge/Autor-Henrique%20C%20C%20de%20Andrade-blue)
[![Updates](https://pyup.io/repos/github/HenriqueCCdA/urlReduce/shield.svg)](https://pyup.io/repos/github/HenriqueCCdA/urlReduce/)
[![codecov](https://codecov.io/gh/HenriqueCCdA/urlReduce/branch/main/graph/badge.svg?token=8U5Z5LSRJ0)](https://codecov.io/gh/HenriqueCCdA/urlReduce)

Nesse repositorio temos o projeto desenvolvido no BootCamp Dev Pro da [PythonPro](www.python.pro.br). O objetivo desse projeto é desenvolver um redutor de url. O link para o deploy da aplicação no **Heroku** pode ser encontrada no link abaixo:

🔥🔥🔥[https://urlreduce.herokuapp.com/](https://urlreduce.herokuapp.com/)🔥🔥🔥



## Principais tecnologias utilizadas:

Necessidade                   | Tecnologias
---------                     | ------
Framework backend             | Django
CI                            | Github Actions
CD                            | Heroku
Banco de dados                | PostgresSQL
Gestão de dependecias         | Pipenv
Testes                        | Pytest 
Relatorio de Erros            | Sentry
Servidor de arquivo estaticos | Whitenose
WSGI                          | Gunicorn 




---

## Passos desensolvidos durante o projeto

### 1) Configuração do projeto 🛠
* criar o ambiente virtual:
       
    ```console
    pipenv install
    ```

* Instalando django:

    ```console
    pipenv install django
    ```

* Instalando o baker
    
    ```console 
    pipenv install -d model-bakery
    ``` 

* Instalando flake8 como dependencia de desenvolimento:

    ```console
    pipenv install -d flake8
    ```

* Instalar o **dj-database-url**

* Configurando o flake8 através do arquivo .flake8

    ```yml
    [flake8]
    max-line-length = 120
    exclude=.venv
    ```

    Esta são apenas as configurações inicias com o tempo elas podem mudar

* Criando o arquivo .gitignore

* Inicializando o projeto **Django**

    ```console
    pipenv shell
    django-admin.exe startproject devpro .
    ```

    Para testar pode-se rodar o servidor através de:

    ```console
    python manage.py runserver
    ```

* Instalando o driver para postgres:

    ```console
    pipenv install psycopg2-binary
    ```

* Instalando a lib python-decouple, criando o arquivo local .env e arquivo versionado contrib/env-sample

   ```yml
   DEBUG=FALSE
   SECRET_KEY=Defina sua chave secreta aqui
   ALLOWED_HOSTS=
   SENTRY_DSN=
   DATABASE_URL=postgres://postgres:postgres@localhost/testedb
   ```

* Criar a aplicação **base**

    ```console
    cd devpro
    python ..\manage.py startapp base
    ```

    Para testar pode-se rodar o servidor através de:

    ```console
    python manage.py runserver
    ```

* Instalando o pytest-django

    ```console
    pipenv install -d 'pytest-django'
    ```

    criar o arquivo pytest.in

    ```yml
    [pytest]
    DJANGO_SETTINGS_MODULE = devpro.settings
    ```

   Rodando os testes.

    ```console
    python -m pytest
    ```

* Instalando a cobertura de testes com **codecov**
 
    ```console 
    pipenv install -d 'pytest-cov' codecov
    ```
* Instalando o ipython e django-extensions

    ```console 
    pipenv install ipython django-extensions 
    ```

    ```python
    INSTALLED_APPS = [
    ... 
    'django_extensions'    
    ]
    ```

* Configurando a coleta dos arquivos estáticos:

    ```python
    STATIC_ROOT = BASE_DIR / 'staticfiles/'
    ```

* Servindo os arquivos estaticos com  o **whitenose**:
  
    ```console
    pipenv install whitenose
    ```


* Instalando o sentry:

    ```console
    pipenv install sentry-sdk
    ```

    Configurando o **SENTRY_DSN** no heroku:

    ```console
    heroku config:set SENTRY_DSN="https://asdasdasdsad"
    ```


* Configurando o **CI**.
    > Link para o GitHub Actions [file](https://github.com/HenriqueCCdA/urlRedure/tree/main/.github/workflows)


* Configurando o **PyUp**

    ```yml
    schedule: ''
    update: false

    requirements:
     - Pipfile
     - Pipfile.lock
    ```

### 2) Deploy no heroku 🛠

* Instalar o arquivo gunicorn:

    ```console
    pipenv install gunicorn
    ```

* Criando o aquivo Procfile:

    ```yaml
    release: python manage.py migrate --noinput
    web: gunicorn devpro.wsgi --log-file -
    ```

* Configurando o postgres

* Crianda apps pelo heroku-cli:

    ```console
    heroku apps:create urlreduce
    ```

* Chave gerando a chave secreta para heroku:

    ```console
    >>>from django.core.management.utils import get_random_secret_key
    >>>get_random_secret_key()
    ```

* Configurando as variaveis no heroku:

    ```console
    heroku config:set DEBUG=False
    heroku config:set SECRET_KEY="chave secreta de verdade"
    ```


* Testando do deploy no heroku:

   ```console
   git push heroku  branch_local:master
   ```

* Configuração para o Deploy automatico é feita no site.



### 3) Iniciando o projeto 🛠

* Criando o app encutador:

    ```console
    cd devpro
    python ../manage.py startapp encurtador
    ```

 * Criando o usuario costumizado:

    > O usuário costumizado irá ficar no aquivos models.py do app encutador. O código base foi retirado da classe AbstracticUser encontrado no módulo django.contib.auth.models.py.

    > Criar UserManager usando novamente a Classe UserManager do módulo django.contib.auth.models.py.


    Criar a varialvel no settings.py

    ```python
    AUTH_USER_MODEL='devpro.encutador'
    ```

    Para testa posse usar o makemigrations

    ```console
    python manage.py makemigrations
    ```

* Redirecionando usando o slug

    ```python
    return redirect(path)  
    ```

* Criando modelo para armazenar as Urls.
    
    > Adicionar CRUD do admin do django.

* Criando a página dos relatórios. 

* Criando modelo para armazenar as UrlLog.

* Mostrando o relatorio



