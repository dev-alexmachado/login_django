from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'data_nascimento', 'comentario']
        widgets = {
                'nome': forms.TextInput(
                        attrs={
                            'id': "email",
                            'required': True,
                        },
                ),
                'email': forms.EmailInput(
                    attrs={
                        'id': "email",
                        'required': True,
                    },
                ),
                'data_nascimento': forms.DateInput(
                    format='%Y-%m-%d',
                    attrs={
                        'type': "date",
                        'id': "data_nascimento",
                        'required': True,
                    },
                ),
                'comentario': forms.Textarea(
                    attrs={
                        'id': "comentario",
                        'rows': 4,
                    },
                ),
        }
        error_messages = {
            'email':{
                'unique': "E-mail já cadastrado.",
            }
        }