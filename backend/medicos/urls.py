from django.urls import path
from medicos import views

app_name = 'medicos'

urlpatterns = [
    path('', views.display_medicos, name="display_medicos"),
    path('search/', views.search, name="search"),
    path('infos/<int:id>', views.infos, name="infos"),
    path('cadastrar/', views.cadastrar_medico, name='cadastrar_medico'),
    path('editar/<int:id>', views.editar_medico, name='editar_medico'),
    path('deletar/<int:id>', views.deletar_medico, name='deletar_medico'),



]