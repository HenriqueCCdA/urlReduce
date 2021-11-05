# 🐍 urlRedure 🐍

[![Updates](https://pyup.io/repos/github/HenriqueCCdA/urlRedure/shield.svg)](https://pyup.io/repos/github/HenriqueCCdA/urlRedure/)
[![codecov](https://codecov.io/gh/HenriqueCCdA/urlRedure/branch/main/graph/badge.svg?token=8U5Z5LSRJ0)](https://codecov.io/gh/HenriqueCCdA/urlRedure)

Projeto desenvolvido no BootCamp Dev Pro do python pro www.python.pro.br. 

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

* Instalando flake8 como dependencia de desenvolimento:

    ```console
    pipenv install -d flake8
    ```

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

* Instalando a lib python-decouple, criando o arquivo local .env e arquivo versionado contrib/env-sample

   ```yml
   DEBUG=FALSE
   SECRET_KEY=Defina sua chave secreta aqui
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



* Configurando o **CI**.  
       Link para o GitHub Actions [file](https://github.com/HenriqueCCdA/urlRedure/tree/main/.github/workflows)


* Configurando o **PyUp**

    ```yml
    schedule: ''
    update: false

    requirements:
     - Pipfile
     - Pipfile.lock
    ```
