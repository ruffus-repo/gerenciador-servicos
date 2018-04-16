from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(u'Nome', max_length=80)
    descricao = models.TextField(verbose_name='Descricao', blank=True, default='')

    def __str__(self):
        return self.nome

class Prestador(models.Model):
    nome = models.CharField(u'Nome', max_length=80)
    endereco = models.CharField(u'Endereco', max_length=100, blank=True, default='')
    telefone = models.CharField(u'Telefone', max_length=20, blank=True, default='')
    observacao = models.TextField(verbose_name='Obsrvacoes', blank=True, default='')
    tipo = models.ForeignKey(Servico, verbose_name='Tipo Servico',on_delete='models.CASCADE')

    def __str__(self):
        return self.nome