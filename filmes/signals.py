from django.db.models.signals import pre_save
from django.dispatch import receiver
from filmes.models import Filme
from API_openai.client import get_filme_sinopse


# O decorator @receiver(receptor) conecta o sinal a uma função
# que será chamada quando o sinal for enviado sender é o 
# modelo que está enviando o sinal, instance é a 
# instância do modelo que está sendo salvo ou deletado
# @receiver(pre_save, sender=Filme)
# def filme_pre_save(sender, instance, **kwargs):
#     print('Filme pre save')
#     print(instance.titulo)

@receiver(pre_save, sender=Filme)
def filme_pre_save(sender, instance, **kwargs):
    if not instance.sinopse:
        IA_sinopse = get_filme_sinopse(
            titulo=instance.titulo,
            ano=instance.ano,
            diretor=instance.diretor,
            atores=instance.atores
        )
        instance.sinopse = IA_sinopse
    
