from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.landing_page, name='pode_aprender'),
    path('cursos/', views.cursos, name='cursos'),
    path('nossa-historia/', views.nossa_historia, name='nossa_historia'),
    path('nossa-equipe/', views.nossa_equipe, name='nossa_equipe'),
]
