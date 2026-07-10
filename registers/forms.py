from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        # Campos que vão aparecer no formulário
        fields = ['nome_completo', 'cpf', 'cargo', 'salario', 'senha']

