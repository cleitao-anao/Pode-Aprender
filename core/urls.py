from django.contrib import admin
from django.urls import include, path
app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.landing_page.urls'), name='home'),
    path('portal_aluno/', include('apps.portal_aluno.urls'), name='portal_aluno')
  
]