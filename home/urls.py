from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.first_page, name="home"),
    path('login/', views.login_page, name="login"),
    path('navegacao/', views.navigation_page, name="navegacao"),
]