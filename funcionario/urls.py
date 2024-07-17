from django.urls import path
from funcionario import views

app_name = 'funcionario'

urlpatterns = [
    path('', views.display_funcionarios, name="display_funcionarios"),
    path('cadastro/', views.cadastrar_funcionario, name="cadastro_funcionario"),
    path('pesquisa/', views.pesquisar_funcionario, name="pesquisa_funcionario"),
    path('editar/<int:id>', views.editar_funcionario, name="edicao_funcionario"),
    path('visualizar/<int:id>', views.infos_funcionario, name="visualizacao_funcionario"),
    path('deletar/<int:id>', views.deletar_funcionario, name="exclusao_funcionario"),
]