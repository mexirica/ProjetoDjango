from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):

    # Seleciona todos os dados do db dados = Fotografia.objects.all()
    dados=Fotografia.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request, foto_id):
    fotografia= get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})