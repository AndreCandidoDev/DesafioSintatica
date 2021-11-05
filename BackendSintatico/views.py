from django.shortcuts import render
from filmes.models import Avaliacao, Filme


def home(request):
    filmes = Filme.objects.all()
    context = {
        'filmes': filmes
    }
    return render(request, 'home.html', context)