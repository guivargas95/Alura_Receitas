from django.shortcuts import get_object_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    #receitas = Receita.objects.all()

    dados = {
        'receitas' : receitas
    }
    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)


def buscar(request):
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