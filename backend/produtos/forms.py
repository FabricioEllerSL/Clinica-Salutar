from django import forms
from django.core.exceptions import ValidationError
from .models import Produto

class ProdutoForm(forms.ModelForm):

    # definindo a classe dos campos que serao renderizados no template cadastro
    # como 'form-input'
    
    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'
            if field_name == 'descricao':
                field.widget.attrs['class'] = 'form-input campo-descricao'


    class Meta:
        model = Produto
        fields = '__all__'