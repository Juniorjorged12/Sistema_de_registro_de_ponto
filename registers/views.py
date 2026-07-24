from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import OperationalError
from .models import Funcionario
from .forms import FuncionarioForm

# Listar funcionários
class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'listar.html'
    context_object_name = 'funcionarios'

    def get_queryset(self):
        try:
            return super().get_queryset()
        except OperationalError:
            return Funcionario.objects.none()

# Criar funcionário
class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar_funcionarios')

# Editar funcionário
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar_funcionarios')

# Deletar funcionário
class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('listar_funcionarios')
