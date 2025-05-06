from django.shortcuts import render, redirect
from filmes.models import Filme
from filmes.forms import FilmesModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class FilmesListView(ListView):
    model = Filme
    template_name = 'filmes.html'
    context_object_name = 'filmes'
    
    def get_queryset(self):
        # super() acessa o queryset padrão da classe ListView (classe pai)
        filmes = super().get_queryset().order_by('titulo')
        search = self.request.GET.get('search')
        if search:
            filmes = filmes.filter(titulo__contains=search)
        return filmes

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
 # dispatch é o método que processa a requisição
class NovoFilmeCreateView(CreateView):
    model = FilmesListView
    form_class = FilmesModelForm
    template_name = 'novo_filme.html'
    success_url = '/filmes/' 

@method_decorator(login_required(login_url='login'), name='dispatch')
class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmesModelForm
    template_name = 'filme_update.html'

    def get_success_url(self):
        return reverse_lazy('filme_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme_delete.html'
    success_url = '/filmes/'    
    
