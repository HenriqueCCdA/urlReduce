# urlRedure

[![Updates](https://pyup.io/repos/github/HenriqueCCdA/urlRedure/shield.svg)](https://pyup.io/repos/github/HenriqueCCdA/urlRedure/)

Projeto desenvolvido no BootCamp Dev Pro do python pro www.python.pro.br.

## Passos desensolvidos 

### configuração do projeto
* criar o ambiente virtual:
       
    ```
    pipenv install
    ```

* Instalando django:

    ```
    pipenv install django
    ```

* Instalando flake8 como dependencia de desenvolimento:

    ```
    pipenv install -d flake8
    ```

* Configurando o flake8 através do arquivo .flake8

    ```
    [flake8]
    max-line-length = 120
    exclude=.venv
    ```

    Esta são apenas as configurações inicias com o tempo elas podem mudar

* Criando o arquivo .gitignore

* Inicializando o projeto **Django**

    ```
    pipenv shell
    django-admin.exe startproject devpro .
    ```

    Para testar pode-se rodar o servidor através de:

    ```
    python manage.py runserver
    ```

* Instalando a lib python-decouple 

* Criar a aplicação **base**

    ```
    cd devpro
    python ..\manage.py startapp base 
    ```

    Para testar pode-se rodar o servidor através de:

    ```
    python manage.py runserver
    ```

* Instalando o pytest-django

    ```
    pipenv install -d 'pytest-django'
    ```

    criar o arquivo pytest.in

    ```
    [pytest]
    DJANGO_SETTINGS_MODULE = devpro.settings
    ```

    Rodando os testes.

    ```
    python -m pytest
    ```

* Instalando a cobertura de testes com **codecov**
 
    ``` 
    pipenv install -d 'pytest-cov' codecov
    ```



* Configurando o **CI**.  

* Configurando o **PyUp**

    ```
    schedule: ''
    update: false

    requirements:
     - Pipfile
     - Pipfile.lock
    ```