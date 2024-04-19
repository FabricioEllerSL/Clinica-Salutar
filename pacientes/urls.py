from django.urls import path
from pacientes import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.display, name="display_pacientes"),
]