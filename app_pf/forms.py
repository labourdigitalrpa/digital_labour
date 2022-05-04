from django import forms
from app_pf.models import clientePfModel
class clientePfForm(forms.ModelForm):
    class Meta:
        model = clientePfModel
        fields = ['nome_completo','cpf', 'chave_ecac', 'senha_ecac', 'email', 'ativo']