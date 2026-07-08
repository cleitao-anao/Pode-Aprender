from django.urls import include, path
from . import views


app_name = 'portal_aluno'
urlpatterns = [
    path('', views.login, name='login'),
  
]