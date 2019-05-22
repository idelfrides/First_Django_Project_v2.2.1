from django.shortcuts import render, redirect

# Create your views here.

# from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm
import datetime


def home(request):
    data = {'transacoes': ['t1', 't2', 't3', 't4'], 'now': datetime.datetime.now()}
    # data = {}
    # data['transacoes'] = ['t1', 't2', 't3', 't4']
    # data['now'] = datetime.datetime.now()
    # html = "<html><body><h1> Data e Hora neste momento: %s.</h1></body></html>"%now
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacap(request):
    data = {}
    formul = TransacaoForm(request.POST or None)

    # validacaodo form
    if formul.is_valid():
        formul.save()
        # return listagem(request)
        return redirect('url_listagem')

    data['form'] = formul
    return render(request, 'contas/form.html', data)


def update(request, mypk):
    dados = {}
    transa = Transacao.objects.get(id=mypk)

    formu = TransacaoForm(request.POST or None, instance=transa)

    if formu.is_valid():
        formu.save()
        return redirect('url_listagem')

    dados['form'] = formu
    dados['transacao'] = transa
    return render(request, 'contas/form.html', dados)


def delete(request, dpk):
    transacao = Transacao.objects.get(id=dpk)
    transacao.delete()
    return redirect('url_listagem')

