from django.urls import path
from . import views


app_name = 'portal_aluno'
urlpatterns = [
    path('', views.login, name='login'),
    path('painel/', views.painel, name='painel'),
    path('grade-horario/', views.grade_horario, name='grade_horario'),
    path('perfil/', views.perfil, name='perfil'),
    path('sair/', views.logout, name='logout'),
]
