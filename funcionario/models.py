from django.db import models

# Create your models here.
class Funcionario(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20, primary_key=True)
    rg = models.CharField(max_length=20)
    num_cart_trab = models.CharField(max_length=20, verbose_name="Numero Carteira de Trabalho")
    cargo = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True, verbose_name="Data de Nascimento")
    rua = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    complemento = models.TextField(blank=True)
    cep = models.CharField(max_length=20, blank=True)
    ponto_referencia = models.TextField(blank=True, verbose_name="Ponto de referência")
    data_admissao = models.DateField(blank=True, null=True, verbose_name="Data da Admissão")
