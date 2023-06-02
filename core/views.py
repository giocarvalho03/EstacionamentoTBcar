from django.shortcuts import render, redirect
from core.forms import *
from core.models import *
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import  messages


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'

@login_required
def cadastroCliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('url_principal')
        contexto = {'form':form, 'txt_titulo':'cad_cli', 'txt_descricao':'Cadastro de Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required()
def listagem_clientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Cliente.objects.filter(nome__contains = request.POST['input_pesquisa'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados':dados , 'text_input':'digite o nome do cliente'}
        return render(request, 'core/listagem_clientes.html', contexto)
    return render(request, 'aviso.html')


@login_required()
def cadastro_veiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_veiculos')
        contexto = {'form': form, 'txt_titulo':'cad_veic', 'txt_descricao':'Cadastro de Veículo' }
        return render(request, 'core/cadastro.html' , contexto)
    return render(request, 'aviso.html')


def home(request):
    return render(request, 'core/index.html')

@login_required()
def altera_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if  request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados do cliente alterado com sucesso!')
                return redirect('url_listagem_clientes')
        contexto = {'form': form, 'txt_titulo':'EditCliente', 'txt_descrição':'Altera Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required()
def listagem_veiculos(request):
    if request.user.is_staff:
        dados = Veiculo.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_veiculos.html', contexto)
    return render(request,'aviso.html')


def exclui_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    contexto = {'txt_info':obj.nome, 'txt_url':'/listagem_clientes/'}
    if request.POST:
        obj.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        contexto.update({'txt_tipo':'Cliente'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def cadastro_rotativo(request):
    form = FormRotativo(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_rotativos')
    else:
        contexto  = {'form': form, 'txt_titulo':'CadRot', 'txt_descricao':'Cadastro de Rotativo'}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)


def listagem_rotativos(request):
    dados = Rotativo.objects.all()
    contexto = {'dados': dados}
    return render(request,  'core/listagem_rotativos.html', contexto)


def altera_rotativo(request, id):
    obj = Rotativo.objects.get(id = id)
    form = FormRotativo(request.POST or None, instance=obj)
    if form.is_valid():
        obj.calcula_total()
        form.save()
        return redirect('url_listagem_rotativos')
    else:
        contexto = {'form':form, 'txt_titulo': 'AltRot', 'txt_descricao':'Altera Rotativo'}
        return render(request, 'core/cadastro.html', contexto)


def exclui_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    contexto = {'txt_info':f'{obj.id_veiculo}-{obj.entrada}', 'txt_url':'/listagem_rotativos/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo':'Rotativo'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def cadastro_tabela(request):
    pass

def listagem_tabelas(request):
    pass