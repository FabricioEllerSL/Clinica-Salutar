from django import forms
from django.core.exceptions import ValidationError
from .models import Medico
from .validators import validar_cpf

class MedicoForm(forms.ModelForm):

    # definindo a classe dos campos que serao renderizados no template cadastro
    # como 'form-input'
    
    def __init__(self, *args, **kwargs):
        super(MedicoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'
            if field_name == 'cpf':
                field.widget.attrs['class'] = 'form-input campo-cpf'
            elif field_name == 'rg':
                field.widget.attrs['class'] = 'form-input campo-rg'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf = cpf.replace('.', '').replace('-', '')
        if not validar_cpf(cpf):
            raise ValidationError('CPF inválido.')
        return cpf
    
    def clean_rg(self):
        rg = self.cleaned_data.get('rg')
        rg = rg.replace('.', '').replace('-', '')
        return rg


    class Meta:
        model = Medico
        fields = '__all__'