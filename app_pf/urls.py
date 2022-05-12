from unicodedata import name
from django.urls import path
from . import views  



urlpatterns = [
    path('', views.index, name='index'),
    path('fomrulario_pf/', views.formulario_pf, name='formulario_pf'),
    path('cadastrarClientePf/',views.cadastrarClientePf,name='cadastrarClientePf'),
    path('visualizarClientePf/<int:pk>/',views.visualizarClientePf,name='visualizarClientePf'),
    path('editarClientePf/<int:pk>/',views.editarClientePf,name='editarClientePf'),
    path('updateClientePf/<int:pk>/',views.updateClientePf,name='updateClientePf'),
    path('deletarClientePf/<int:pk>/',views.deletarClientePf,name='deletarClientePf'),
    
    ]
