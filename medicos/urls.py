from django.urls import path
from medicos import views

app_name = 'medicos'

urlpatterns = [
    path('', views.display_medicos, name="display_medicos"),
    path('search/', views.search, name="search"),
    path('infos/<int:id>', views.infos, name="infos"),


]