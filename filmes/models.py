from django.db import models

class Ator(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

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
    atores = models.ManyToManyField(Ator, 
                                    related_name='filmes', 
                                    blank=True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.titulo

