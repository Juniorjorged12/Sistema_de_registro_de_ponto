from django.shortcuts import render, get_object_or_404
from django.utils.dateparse import parse_date
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.timezone import localtime
from registers.models import Funcionario
from .models import RegistroPonto


def registrar_ponto(request):
    hora_atual = localtime()
    mensagem = ""
    if request.method == "POST":
        senha = request.POST.get("senha")
        try:
            funcionario = Funcionario.objects.get(senha=senha)
            # Verifica se já existe ponto aberto
            ponto_aberto = RegistroPonto.objects.filter(funcionario=funcionario, aberto=True).first()
            if ponto_aberto:
                # Fecha o ponto
                ponto_aberto.data_hora_saida = hora_atual
                ponto_aberto.aberto = False
                ponto_aberto.save()
                mensagem = f"Ponto fechado para {funcionario.nome_completo} às {ponto_aberto.data_hora_saida}."
            else:
                # Abre novo ponto
                novo_ponto = RegistroPonto.objects.create(
                    funcionario=funcionario,
                    data_hora_entrada=hora_atual,
                    aberto=True
                )
                mensagem = f"Ponto aberto para {funcionario.nome_completo} às {novo_ponto.data_hora_entrada}."
        except Funcionario.DoesNotExist:
            mensagem = "Senha inválida. Funcionário não encontrado."
    return render(request, "registrar.html", {"mensagem": mensagem})


def relatorio_pontos(request):
    funcionarios = Funcionario.objects.all()
    dados = []

    for funcionario in funcionarios:
        registros = RegistroPonto.objects.filter(funcionario=funcionario).order_by('-data_hora_entrada')
        dados.append({
            'funcionario': funcionario,
            'registros': registros
        })

    return render(request, 'relatorio.html', {'dados': dados})


def relatorio_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    registros = RegistroPonto.objects.filter(funcionario=funcionario).order_by('-data_hora_entrada')

    # Captura as datas enviadas pelo formulário
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if data_inicio and data_fim:
        registros = registros.filter(
            data_hora_entrada__date__range=[parse_date(data_inicio), parse_date(data_fim)]
        )

    return render(request, 'relatorio_funcionario.html', {
        'funcionario': funcionario,
        'registros': registros,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    })


def relatorio_funcionario_pdf(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    registros = RegistroPonto.objects.filter(funcionario=funcionario).order_by('-data_hora_entrada')

    # Captura os filtros de data da URL
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if data_inicio and data_fim:
        registros = registros.filter(
            data_hora_entrada__date__range=[parse_date(data_inicio), parse_date(data_fim)]
        )

    # Renderiza o template PDF
    template_path = 'relatorio_funcionario_pdf.html'
    context = {
        'funcionario': funcionario,
        'registros': registros,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    }
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="relatorio_{funcionario.nome_completo}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', status=500)
    return response