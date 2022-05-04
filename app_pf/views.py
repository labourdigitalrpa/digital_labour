from django.shortcuts import render, redirect
from app_pf.forms import clientePfForm

def index(request):
    return render(request, 'index.html')

def formulario_pf(request):
    data = {}
    data['form'] = clientePfForm()
    return render(request, 'formulario_pf.html', data)

def cadastrarClientePf(request):
    form = clientePfForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

