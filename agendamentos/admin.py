from django.contrib import admin
from .models import Agendamento

# Register your models here.

@admin.register(Agendamento)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('data', 'nome_paciente')