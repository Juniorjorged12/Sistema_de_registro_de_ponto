from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import OperationalError, DatabaseError
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['funcionarios'] = list(self.get_queryset())
        except OperationalError:
            context['funcionarios'] = []
        return context

# Criar funcionário
class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar_funcionarios')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except (OperationalError, DatabaseError):
            form.add_error(None, 'Não foi possível salvar o funcionário no momento. O banco ainda não está pronto.')
            return self.form_invalid(form)

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
