from django import forms
from django.core.exceptions import ValidationError
from .models import Funcionario
from pacientes.validators import validar_cpf


class FuncionarioForm(forms.ModelForm):

    # definindo a classe dos campos que serao renderizados no template cadastro
    # como 'form-input'
    
    def __init__(self, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not validar_cpf(cpf):
            raise ValidationError('CPF inválido.')
        return cpf


    class Meta:
        model = Funcionario
        fields = '__all__'