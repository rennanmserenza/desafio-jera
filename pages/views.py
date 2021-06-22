from django.views.generic import TemplateView, ListView
import requests

class HomePageView(TemplateView):
    template_name = "home.html"


class SearchResultViews(ListView):
    template_name = "search_results.html"

    def search_movie():    

        API_KEY = 'api_key=70631fbbad5107d70d2fd3ebc0d78e77'
        path_main = 'https://api.themoviedb.org/3/'

        movie_search = input('Digite o nome do filme que deseja pesquisar: ')
        movie_search_path = f'query={movie_search}'

        url_path = f'{path_main}search/movie?{API_KEY}&language=pt-BR&{movie_search_path}&page=1&include_adult=false'

        search = requests.get(url_path)
        resposta = search.json()

        lista_de_filmes = list()
        busca = dict()

        for i, filmes in enumerate(resposta["results"], start=1):
            busca[f'Filme'] = i
            filme = dict()

            for index in filmes:
                if index in ['id', 'original_title', 'overview', 'original_language', 'vote_average']:
                    filme[index] = filmes[index]

            busca['informação'] = filme.copy()
            lista_de_filmes.append(busca.copy())

        # for filmes in lista_de_filmes:
        #     for k, v in filmes['informação'].items():
        #         print(f'A chave é {k} e o valor é {v}.')
        #     print()

        return lista_de_filmes