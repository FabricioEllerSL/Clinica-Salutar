from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CadastrarUsuarioForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', forms.ValidationError("Email ja cadastrado", code='invalid'))

        return email
    

