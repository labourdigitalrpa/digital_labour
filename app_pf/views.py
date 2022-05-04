from django.shortcuts import render
from app_pf.forms import clientePfForm

def index(request):
    return render(request, 'index.html')

def formulario_pf(request):
    data = {}
    data['form'] = clientePfForm()
    return render(request, 'formulario_pf.html', data)