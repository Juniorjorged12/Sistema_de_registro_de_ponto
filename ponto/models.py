from django.db import models
from django.utils import timezone
from registers.models import Funcionario

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='registros_ponto')
    data_hora_entrada = models.DateTimeField(null=True, blank=True)
    data_hora_saida = models.DateTimeField(null=True, blank=True)
    aberto = models.BooleanField(default=False)

    @property
    def horas_trabalhadas(self):
        if self.data_hora_entrada and self.data_hora_saida:
            delta = self.data_hora_saida - self.data_hora_entrada
            total_minutes = int(delta.total_seconds() // 60)
            hours = total_minutes // 60
            minutes = total_minutes % 60
            return f"{hours}h {minutes}m"
        return "-"

    def __str__(self):
        return f"{self.funcionario.nome_completo} - {self.data_hora_entrada} / {self.data_hora_saida}"
