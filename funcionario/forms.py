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
            if field_name == 'cpf':
                field.widget.attrs['class'] = 'form-input campo-cpf'
            elif field_name == 'cep':
                field.widget.attrs['class'] = 'form-input campo-cep'
            elif field_name == 'data_nascimento' or field_name == 'data_admissao':
                field.widget.attrs['class'] = 'form-input campo-data'
            elif field_name == 'telefone':
                field.widget.attrs['class'] = 'form-input campo-telefone'
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
    
    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        cep = cep.replace('-', '')
        return cep
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        telefone = telefone.replace('(', '').replace(')', '').replace('-', '')
        return telefone


    class Meta:
        model = Funcionario
        fields = '__all__'