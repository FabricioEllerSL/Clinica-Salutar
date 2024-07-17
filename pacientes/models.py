from django.db import models

# Create your models here.

class Paciente(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20, unique=True)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.TextField(blank=True)
    cep = models.CharField(max_length=20)
    ponto_referencia = models.TextField(blank=True)
    nome_mae = models.CharField(max_length=50, blank=True)
    nome_pai = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=20)