from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=280)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.descricao