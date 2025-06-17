from filmes.models import Filme
from filmes.forms import FilmesModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

class FilmesListView(ListView):
    model = Filme
    template_name = 'filmes.html'
    context_object_name = 'filmes'
    
    def get_queryset(self):
        filmes = super().get_queryset().order_by('titulo')
        titulo = self.request.GET.get('titulo')
        ator = self.request.GET.get('ator')

        if titulo:
            filmes = filmes.filter(titulo__icontains=titulo)

        if ator:
            filmes = filmes.filter(atores__nome__icontains=ator)

        return filmes

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
 # dispatch é o método que processa a requisição
class NovoFilmeCreateView(CreateView):
    model = Filme
    form_class = FilmesModelForm
    template_name = 'novo_filme.html'
    success_url = '/filmes/'

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.save()
    #     form.save_m2m()
    #     return super().form_valid(form) 


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
    
