from django.urls import path
from agendamentos import views

app_name = 'agendamentos'

urlpatterns = [
    path('', views.display, name="display_agendamentos"),
    path('cadastrar/', views.cadastrar_agendamento, name="cadastrar_agendamento"),
    path('search/', views.search, name="search"),
    path('editar/<int:id>', views.editar_agendamento, name="editar_agendamento"),
    path('infos/<int:id>', views.infos, name="infos"),
    path('deletar/<int:id>', views.deletar_agendamento, name="deletar_agendamento"),

]