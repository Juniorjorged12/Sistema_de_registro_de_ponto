from django.db import models
from django.core.validators import RegexValidator

senha_validator = RegexValidator(
    regex=r'^\d{4}$',
    message="A senha deve conter exatamente 4 dígitos numéricos."
)

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    senha = models.CharField(
        max_length=4,
        unique=True,
        validators=[senha_validator],
        help_text="Senha numérica de 4 dígitos"
    )

    def __str__(self):
        return self.nome_completo

