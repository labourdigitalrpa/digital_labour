from django.shortcuts import render, redirect
from app_pf.forms import clientePfForm
from app_pf.models import clientePfModel

def index(request):
    data_index = {}
    data_index['db'] = clientePfModel.objects.all().order_by('nome_completo')
    return render(request, 'index.html', data_index)

def formulario_pf(request):
    data_formulario_pf = {}
    data_formulario_pf['form'] = clientePfForm()
    return render(request, 'formulario_pf.html', data_formulario_pf)

def cadastrarClientePf(request):
    form = clientePfForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

def visualizarClientePf(request, pk):
    data_visualizarClientePf = {}
    data_visualizarClientePf['db'] = clientePfModel.objects.get(pk=pk)
    return render(request, 'visualizar_pf.html',data_visualizarClientePf)

def editarClientePf(request, pk):
    data_editarClientePf = {}
    data_editarClientePf['db'] = clientePfModel.objects.get(pk=pk)
    data_editarClientePf['form'] = clientePfForm(instance=data_editarClientePf['db'])
    return render(request, 'formulario_pf.html', data_editarClientePf) 

def updateClientePf(request,pk):
    data_updateClientePf = {}
    data_updateClientePf['db'] = clientePfModel.objects.get(pk=pk)
    form_updateClientePf = clientePfForm(request.POST, instance=data_updateClientePf['db'])
    if form_updateClientePf.is_valid():
        form_updateClientePf.save()
        return redirect('index')



def deletarClientePf(request, pk):
    data_deletaCliente = clientePfModel.objects.get(pk=pk)
    data_deletaCliente.delete()
    return redirect('index')
        

