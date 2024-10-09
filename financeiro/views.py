from django.shortcuts import render, redirect
from .models import Lancamento
from .forms import LancamentoForm

def index(request):
    # Processar o formulário de lançamento
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto no banco de dados
            return redirect('index')  # Redireciona para a página inicial
        else:
            print(form.errors)  # Imprime os erros do formulário no console
    else:
        form = LancamentoForm()

    # Recuperando lançamentos e calculando saldo
    lancamentos = Lancamento.objects.all().order_by('data')
    saldo = 0
    receitas = 0
    despesas = 0

    # Labels e dados para o gráfico
    labels = []
    data = []

    for lancamento in lancamentos:
        if lancamento.tipo == 'credito':
            saldo += lancamento.valor
            receitas += lancamento.valor
        elif lancamento.tipo == 'debito':
            saldo -= lancamento.valor
            despesas += lancamento.valor

        # Adiciona as datas e saldos ao gráfico
        labels.append(lancamento.data.strftime('%d/%m/%Y'))
        data.append(float(saldo))  # Garantir que os valores sejam números

    contexto = {
        'form': form,
        'lancamentos': lancamentos,
        'saldo': saldo,
        'receitas': receitas,
        'despesas': despesas,
        'resultado': receitas - despesas,
        'labels': labels,
        'data': data,
    }
    return render(request, 'financeiro/index.html', contexto)
