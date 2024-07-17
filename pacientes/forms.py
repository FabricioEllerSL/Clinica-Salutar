from django import forms
from django.core.exceptions import ValidationError
from .models import Paciente
from .validators import validar_cpf

class PacienteForm(forms.ModelForm):

    # definindo a classe dos campos que serao renderizados no template cadastro
    # como 'form-input'
    
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'
            if field_name == 'cpf':
                field.widget.attrs['class'] = 'form-input campo-cpf'
            elif field_name == 'cep':
                field.widget.attrs['class'] = 'form-input campo-cep'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf = cpf.replace('.', '').replace('-', '')
        if not validar_cpf(cpf):
            
            raise ValidationError('CPF inválido.')
        return cpf
    
    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        cep = cep.replace('-', '')
        return cep


    class Meta:
        model = Paciente
        fields = '__all__'