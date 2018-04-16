from django.shortcuts import render, redirect
from .models import Servico, Prestador
import subprocess
from subprocess import call

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

class ServicoListView(ListView):
    model = Servico

class ServicoDetailView(DetailView):
    model = Servico

class ServicoCreateView(CreateView):
    model = Servico
    fields = '__all__'
    success_url = '/servicos/servico-list/'

class PrestadorListView(ListView):
    model = Prestador

class PrestadorDetailView(DetailView):
    model = Prestador

def gerarArquivo(request):
    subprocess.call(["/home/doyle/chamapython"])
    return redirect('prestador-list')