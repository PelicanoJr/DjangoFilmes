from django.db import models

class Genero(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome    

class Filme(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField(blank=True, null=True)
    duracao = models.IntegerField()
    ano = models.IntegerField() 
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filmes')
    diretor = models.CharField(max_length=100)
    atores = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.titulo

# 