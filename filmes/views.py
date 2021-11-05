from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Avaliacao, Filme
from .forms import AvaliacaoForm

import statistics


def avaliacoes_list(request, id):
    filme = Filme.objects.get(id=id)
    avaliacoes_filme = filme.avaliacoes.all()
    total = avaliacoes_filme.count()
    aux = []
    for avaliacao in avaliacoes_filme:
        aux.append(avaliacao.avaliacao)
    try:
        media = statistics.mean(aux)
    except:
        media = None
    context = {
               'filme': filme,
               'avaliacoes': avaliacoes_filme,
               'total': total,
               'media': media
               }
    return render(request, 'filmes/listaavaliacoes.html', context)


def avaliacao_create(request, id):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST or None)
        filme = Filme.objects.get(id=id)
        if form.is_valid():
            nome_completo = form.cleaned_data['nome_completo']
            email = form.cleaned_data['email']
            avaliacao = form.cleaned_data['avaliacao']
            comentario = form.cleaned_data['comentario']
            av = Avaliacao.objects.create(nome_completo=nome_completo, email=email, avaliacao=avaliacao,
                                          comentario=comentario)
            av.save()
            filme.avaliacoes.add(av)
            return redirect('home')
    else:
        form = AvaliacaoForm()
    context = {'form': form}
    return render(request, 'filmes/criaravaliacao.html', context)
