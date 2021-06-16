# desafio-jera
Criar uma aplicação que consome uma API de filmes.

Primeiro passo após clonar o repositório, ativar a venv do python
-> cd \venv\Scripts, dentro de Scripts já de o comando activate.
(venv) PS C:\desafio-jera>
ficara parecido com algo assim.

Instale o Django agr na sua virtualenv com o comando py -m pip install Django

após instalado, rode o comando py manage.py migrate para criar seu DB com SQLite3

Então sua aplicação está pronta para rodar com o código py manage.py runserver

Caso queira criar um superuser para acessar o admin do Django rode o comando
py manage.py createsuperuser
