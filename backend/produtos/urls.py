from django.urls import path
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('', views.display_produtos, name="display_produtos"),
    path('cadastrar/', views.cadastrar_produto, name="cadastrar_produto"),
    path('search/', views.search, name="search"),
    path('infos/<int:id>', views.infos, name="infos"),
    path('editar/<int:id>', views.editar_produto, name='editar_produto'),
    path('deletar/<int:id>', views.deletar_produto, name='deletar_produto'),


]