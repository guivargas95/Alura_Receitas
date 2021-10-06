from django.shortcuts import render, redirect, get_object_or_404
from recipes.models import Receita
from django.contrib.auth.models import User
from django.contrib import auth, messages

def buscar(request):
    '''Realiza busca das receitas pelo título''' 

    lista_receitas = Receita.objects.filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar != '':
            lista_receitas = lista_receitas.filter(nome_receita__contains=nome_a_buscar)
        else:
            lista_receitas = lista_receitas.objects.order_by('-data_receita').filter(publicada=True)


    dados = {
        'receitas' : lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)

