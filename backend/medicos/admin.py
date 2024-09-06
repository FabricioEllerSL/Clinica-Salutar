from django.contrib import admin
from .models import Medico

# Register your models here.

@admin.register(Medico)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')