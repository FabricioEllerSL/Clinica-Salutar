from django.contrib import admin
from .models import Funcionario

# Register your models here.

@admin.register(Funcionario)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')