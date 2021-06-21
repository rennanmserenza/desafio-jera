from django.db import models
from django.conf import settings

class FilmeList(models.Model):
    usuário = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lista_de_filmes_para_assistir = []
