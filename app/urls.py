
from django.contrib import admin
from django.urls import path
from registers import views as register_views
from ponto import views as ponto_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_views.FuncionarioListView.as_view(), name='listar_funcionarios'),
    path('novo/', register_views.FuncionarioCreateView.as_view(), name='criar_funcionario'),
    path('editar/<int:pk>/', register_views.FuncionarioUpdateView.as_view(), name='editar_funcionario'),
    path('deletar/<int:pk>/', register_views.FuncionarioDeleteView.as_view(), name='deletar_funcionario'),

    path('registrar_ponto/', ponto_views.registrar_ponto, name='registrar_ponto'),
    path('relatorio_pontos/', ponto_views.relatorio_pontos, name='relatorio_pontos'),
    path('relatorio_funcionario/<int:id>/', ponto_views.relatorio_funcionario, name='relatorio_funcionario'),
    path('relatorio_funcionario_pdf/<int:id>/', ponto_views.relatorio_funcionario_pdf, name='relatorio_funcionario_pdf'),
    
]
