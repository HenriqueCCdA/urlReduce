# urlRedure

Projeto desenvolvido no BootCamp Dev Pro do python pro www.python.pro.br.

## Passos desensolvidos 

### configuração do projeto
    1. criar o ambiente virtual:
       
    ```
    pipenv install
    ```

    2. Instalando django:

    ```
    pipenv install django
    ```

    3. Instalando flake8 como dependencia de desenvolimento:

    ```
    pipenv install -d flake8
    ```

    4. Configurando o flake8 através do arquivo .flake8

    ```
    [flake8]
    max-line-length = 120
    exclude=.venv
    ```

    Esta são apenas as configurações inicias com o tempo elas podem mudar

    5. Criando o arquivo .gitignore

    6. Inicializando o projeto **Django**

    ```
    pipenv shell
    django-admin.exe startproject devpro .
    ```

    Para testar pode-se rodar o servidor através de:

    ```
    python manage.py runserver
    ```
