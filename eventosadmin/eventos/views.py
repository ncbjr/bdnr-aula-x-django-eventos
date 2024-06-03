# eventos/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone  # Adicione esta linha
from .models import Evento
from .forms import EventoForm

def pagina_inicial(request):
    eventos = Evento.objects.filter(data_hora_inicio__gte=timezone.now()).order_by('data_hora_inicio')
    return render(request, 'eventos/pagina_inicial.html', {'eventos': eventos})

def detalhe_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'eventos/detalhe_evento.html', {'evento': evento})

@login_required
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user
            evento.save()
            return redirect('detalhe_evento', id=evento.id)
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})

@login_required
def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if evento.criador != request.user:
        return redirect('pagina_inicial')
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalhe_evento', id=evento.id)
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form})

@login_required
def excluir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if evento.criador == request.user:
        evento.delete()
    return redirect('pagina_inicial')
