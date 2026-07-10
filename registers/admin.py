from django.contrib import admin
from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'cargo', 'salario', 'senha')
    list_filter = ('cargo',)
    search_fields = ('nome_completo', 'cpf', 'senha')
    ordering = ('nome_completo',)

