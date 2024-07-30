from django.db import models

# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20, unique=True)
    rg = models.CharField(max_length=20)
    numero_classe = models.CharField(max_length=20)
    profissao = models.CharField(max_length=20)