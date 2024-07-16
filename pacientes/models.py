from django.db import models

# Create your models here.

class Paciente(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20, primary_key=True)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    rua = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    complemento = models.TextField(blank=True)
    cep = models.CharField(max_length=20, blank=True)
    ponto_referencia = models.TextField(blank=True)
    nome_mae = models.CharField(max_length=50, blank=True)
    nome_pai = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=20)