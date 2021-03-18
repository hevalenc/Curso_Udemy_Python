#aula sobre Django

#criando um projeto Django no python : django-admin startproject projeto .
#'projeto .' - criando uma pasta com o nome 'projeto'

#iniciar um projeto no python: python manage.py startapp blog
#vai ser criado uma pasta como nome do app

#para rodar um servidor python para executar o projeto django: python manage.py runserver

"""
Todo app criado no djando deve ser registrado no arquivo settings.py e urls.py da pasta principal, nesta aula é a
pasta projeto.

No arquivo settings.py, o app será registrado no módulo INSTALLED_APPS
No arquivo urls.py, deve ser adicionado a linha de comando abaixo no campo  "urlpatterns"
    "path('blog/', include('blog.urls')),"

Obs.: O arquivo urls.py da pasta blog foi criado manualmente

Todo arquivo url deve ter estes módulos importados:

from django.urls import path
from . import views #o '.' referencia a própria pasta do arquivo

As pastas projeto, blog, produto e sobre pertencem a esta aula
A pasta/projeto vdjando é relacionada com esta aula
"""
"""
No arquivo settings.py da pasta principal do projeto, o template que será usado em todo o projeto será mencionado no
campo 'TEMPLATES' na linha 'DIRS' -> 'DIRS': [os.path.join(BASE_DIR, 'paginas')], onde BASE_DIR - base do diretório
e paginas - local do arquivo que será o template principal do projeto. Obs.: importar o built-in 'os'
"""