from django.db import models

# Create your models here.

class Paciente(models.Model):

    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20, primary_key=True)
    nome_pai = models.CharField(max_length=50)
    nome_mae = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=50)
    complemento = models.TextField()
    cep = models.CharField(max_length=20)
    ponto_referencia = models.TextField()