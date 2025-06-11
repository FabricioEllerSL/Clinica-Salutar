from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from agendamentos.models import Agendamento
from pacientes.models import Paciente
from medicos.models import Medico

class AgendamentoForm(forms.ModelForm):

    # definindo a classe dos campos que serao renderizados no template cadastro
    # como 'form-input'
    
    def __init__(self, *args, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'
            if field_name == 'data':
                field.widget.attrs['class'] = 'form-input campo-data'
            if field_name == 'horario':
                field.widget.attrs['class'] = 'form-input campo-horario'

    nome_paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        label="Paciente",
        widget=forms.Select,
        empty_label="Selecione um paciente",
        to_field_name="nome",
    )

    nome_medico = forms.ModelChoiceField(
        queryset=Medico.objects.all(),
        label="Médico",
        widget=forms.Select,
        empty_label="Selecione um médico",
        to_field_name="nome",
    )

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data < date.today():
            raise ValidationError("A data do agendamento não pode ser menor que a data atual.")
        return data


    class Meta:
        model = Agendamento
        fields = '__all__'