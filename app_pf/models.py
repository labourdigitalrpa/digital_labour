from django.db import models

class clientePfModel(models.Model):
    nome_completo = models.CharField(max_length=40, unique=True)
    cpf = models.CharField(max_length=14 , unique=True)
    chave_ecac = models.CharField(max_length=14 , unique=True)
    senha_ecac = models.CharField(max_length=14)
    email = models.EmailField(max_length=40)
    ativo = models.BooleanField(default=True)
