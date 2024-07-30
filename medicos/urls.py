from django.urls import path
from medicos import views

app_name = 'medicos'

urlpatterns = [
    path('', views.display_medicos, name="display_medicos"),


]