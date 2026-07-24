from unittest.mock import patch

from django.db import OperationalError
from django.test import TestCase
from django.urls import reverse

from .forms import FuncionarioForm
from .models import Funcionario


class HomePageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('listar_funcionarios'))
        self.assertEqual(response.status_code, 200)


class FuncionarioFormTests(TestCase):
    def test_form_handles_database_error_during_unique_validation(self):
        data = {
            'nome_completo': 'Maria Souza',
            'cpf': '12345678901',
            'cargo': 'Analista',
            'salario': '2500.00',
            'senha': '1234',
        }

        form = FuncionarioForm(data=data)

        with (
            patch.object(Funcionario, 'validate_unique', side_effect=OperationalError('no such table')),
            patch('registers.forms.call_command', side_effect=OperationalError('migrate failed')),
        ):
            is_valid = form.is_valid()

        self.assertFalse(is_valid)
        self.assertIn('Não foi possível validar', str(form.errors['__all__'][0]))
