from django.urls import path
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('', views.display_produtos, name="display_produtos"),
    path('cadastrar/', views.cadastrar_produto, name="cadastrar_produto"),
    path('search/', views.search, name="search"),
]