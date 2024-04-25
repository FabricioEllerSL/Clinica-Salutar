from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.first_page, name="home"),
    path('cadastro/', views.create_user, name="cadastro"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('navegacao/', views.navigation_page, name="navegacao"),
]