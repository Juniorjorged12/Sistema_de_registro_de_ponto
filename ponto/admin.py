from django.contrib import admin
from .models import RegistroPonto

@admin.register(RegistroPonto)
class RegistroPontoAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'data_hora_entrada', 'data_hora_saida', 'aberto')
    list_filter = ('aberto', 'funcionario')
    search_fields = ('funcionario__nome_completo', 'funcionario__cpf')
    ordering = ('-data_hora_entrada',)
