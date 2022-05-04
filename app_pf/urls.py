from unicodedata import name
from django.urls import path
from . import views  



urlpatterns = [
    path('', views.index, name='index'),
    path('fomrulario_pf/', views.formulario_pf, name='formulario_pf'),
    path('cadastrarClientePf/',views.cadastrarClientePf,name='cadastrarClientePf'),
    ]