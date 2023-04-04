from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    # Seleciona todos os dados do db dados = Fotografia.objects.all()
    dados=Fotografia.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request, foto_id):
    fotografia= get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    dados=Fotografia.objects.order_by("data").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscar=request.GET['buscar']
        if nome_buscar:
            dados=dados.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/buscar.html', {'cards': dados})