from django.urls import path
from pacientes import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.display, name="display_pacientes"),
    path('search/', views.search, name="search"),
    path('infos/<int:id>', views.infos, name="infos"),
    path('cadastrar/', views.cadastrar_paciente, name='cadastro_paciente'),
    path('editar/<int:id>', views.editar_paciente, name='editar_paciente'),
    path('deletar/<int:id>', views.deletar_paciente, name='deletar_paciente'),

]