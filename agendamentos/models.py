from django.db import models

from medicos.models import Medico
from pacientes.models import Paciente

# Create your models here.

class Agendamento(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    nome_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)