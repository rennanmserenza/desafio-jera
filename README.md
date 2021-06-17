## 📋 Sobre
  Este projeto está sendo desenvolvido, para o desafio fornecido para uma vaga na empresa Jera.

  Nele foi realizada a criação de um site que consome uma api de filmes, themovieDB : [TMDB](https://www.themoviedb.org/?language=pt-BR).


## 📋 Objetivo geral

    Desenvolver uma aplicação Web ou Mobile para o armazenamento de uma lista de filmes que o usuário gostaria de assistir. Essa lista deverá ser pega pela API do TheMovieDB.
    Uma conta pode ser vinculada a mais de um perfil, sendo obrigatório ter ao menos um perfil vinculado. A lista de filmes deverá estar associada ao perfil, não a conta, por exemplo: o perfil Filho deverá ter uma lista de filmes a assistir, já o perfil Mãe pode ter outros filmes a assistir (como funciona no Netflix). 


## 📚 Assuntos aplicados

Nesse desafio foram cobrados e aplicados os seguintes conceitos:

    - Criar conta

        Como um usuário gostaria de criar uma conta na plataforma, sendo essa conta privada, onde outras contas não possam ver as minhas listas.

            -- A conta deverá ter um perfil principal contendo: email, senha, nome e data de nascimento.
            -- A aplicação não deve ter mais de uma conta  associada ao mesmo email.


    - Login da conta

        Como usuário gostaria de logar na plataforma e continuar a visualizar as minhas listas.

            -- Login será feito por: email e senha
            -- Todas as áreas privadas só podem ser acessadas caso o usuário esteja autenticado.(O acesso direto por URL não deve ser permitido, caso o usuário não esteja logado.)

    - Criar Perfil

        Como um usuário gostaria de criar diferentes perfis de usuários, para que eu possa associar os filmes a cada perfil, deixando a minha lista de filmes organizada.
            
            -- O perfil deverá ter somente um nome.
            -- O usuário pode ter no máximo quatro perfis.

    - Listar perfis

        Como usuário gostaria de ver todos os perfis associados a minha conta para selecionar o perfil desejado e ter o conteúdo filtrado.
            
            -- Lista de todos os perfis associados ao usuário.
            -- Os conteúdos internos da aplicação serão definidos a partir de um perfil selecionado.

    - Lista de filmes sugeridos

        Como usuário gostaria de ter uma lista de filmes personalizada para o meu perfil, para que eu gaste menos tempo selecionando o que eu gostaria de assistir.

            -- A lista personalizada depende dos filmes que o usuário adiciona na lista de filmes e filmes já assistidos
            -- O predominante da lista é as categorias dos filmes que estão na lista ou já foram assistidos (Não precisa ter inteligência, é uma busca por filmes das categorias que o perfil, mais assiste.)

    - Busca de filmes

        Como usuário gostaria de ter a opção de buscar um filme a partir de um texto qualquer, para que eu possa localizar filmes que não estão listados em meus filmes sugeridos.

            -- Busca de filmes por termo.

    - Marcar filme como para assistir

        Como usuário gostaria de marcar um filme para assistir, para que eu não esqueça dos filmes que eu me interessei.

            -- Filmes marcado como watchlist deve ser salvo no perfil do usuário.
            -- Os filmes no watchlist devem ser levados em consideração na sugestão de filmes.

    - Visualizar lista para assistir

        Como usuário gostaria de visualizar a lista para assistir que criei de uma forma rápida e sucinta.

            -- Lista de filmes que foram marcados em determinado perfil


## 💾 Framework e linguagem utilizados

    Para criação deste projeto foi escolhida a linguagem python(na versão 3.9.1), por ser a que mais possuo familiaridade, apesar de também me interessar por javascript.
    
    Com a linguagem de programação enfim definida optei pelo framework Django por ter uma ótima documentação e por agregar muito ao projeto sem muitas configurações iniciais, como por exemplo já vir com uma configuração de banco de dados pronta para desenvolvimento, podendo ser facilmente trocado para momento de produção caso este seja necessário.


## 💾 Como utilizar 

Primeiramente clone o projeto
      
    git clone https://github.com/rennanmserenza/desafio-jera.git

Depois ative a virtualenv, tenha certeza de ter o python e o django instalados
    Para instalação do django se for preciso

    pip3 install django

    Dirija-se a pasta de Scripts
    
    cd \venv\Scripts

    Caso esteja no cmd o comando "activate" já bastará para coloca-la em funcionamento mas caso não seja o suficiente use

    .\activate

    após a ativação você deverá ver algo parecido com isto no seu shell 

    (venv) PS C:\desafio-jera>

Com nossa virtualenv ativa volte para o diretório principal e execute o comando

    py manage.py migrate

este comando irá criar nosso banco de dados para testes

Para rodar nossa aplicação utilizaremos o seguinte comando

    py manage.py runserver

Caso queira criar um super user para acessar a parte de admin do django é só utilizar o comando

    py manage.py createsuperuser
