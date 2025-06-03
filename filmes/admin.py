from django.contrib import admin
from filmes.models import Filme
from filmes.models import Genero
from filmes.models import Ator

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'genero', 'diretor')
    search_fields = ('titulo', 'ano', 'diretor')
    filter_horizontal = ('atores',)
admin.site.register(Filme, FilmeAdmin)   

class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento')
    search_fields = ('nome',)
admin.site.register(Ator, AtorAdmin)

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
admin.site.register(Genero, GeneroAdmin)