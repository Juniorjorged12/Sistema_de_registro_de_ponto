from django import forms
from django.core.management import call_command
from django.db import DatabaseError, OperationalError

from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome_completo', 'cpf', 'cargo', 'salario', 'senha']
        widgets = {
            'nome_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00',
            }),
            'cargo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Analista',
            }),
            'salario': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': '0.00',
            }),
            'senha': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha',
            }),
        }

    def is_valid(self):
        try:
            return super().is_valid()
        except (OperationalError, DatabaseError):
            try:
                call_command('migrate', interactive=False, verbosity=0)
                return super().is_valid()
            except Exception:
                self.add_error(None, 'Não foi possível validar os dados no momento. O banco ainda não está pronto.')
                return False

