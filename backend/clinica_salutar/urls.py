"""
URL configuration for clinica_salutar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pacientes.views import PacienteViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # urls antigo frontend

    path('', include('home.urls')),
    # path('pacientes/', include('pacientes.urls')),
    # path('funcionario/', include('funcionario.urls')),
    # path('produtos/', include('produtos.urls')),
    # path('medicos/', include('medicos.urls')),
    # path('agendamentos/', include('agendamentos.urls')),

    # urls da api

    path('api/v1/', include(router.urls)),
]