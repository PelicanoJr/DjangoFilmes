from django.contrib import admin
from filmes.models import Filme
from filmes.models import Genero

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'genero', 'diretor', 'atores')
    search_fields = ('titulo', 'ano', 'genero', 'diretor', 'atores')

admin.site.register(Filme, FilmeAdmin)    

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Genero, GeneroAdmin)