from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import home, empresas, empresasDelete, empresaEdit, contratante, contratanteDelete, contratanteEdit, musico, musicoDelete, musicoEdit
from .views import produtor, produtorDelete, produtorEdit, tecnico, tecnicoDelete, tecnicoEdit
urlpatterns = [
    path('', home, name='home'),


    # EMPRESAS
    path('empresas/', empresas, name='empresas'),
    path('deleteempresa/<int:pk>/', empresasDelete, name='empresa_delete'),
    path('updateempresa/<int:pk>/', empresaEdit, name='empresa_edit'),

    # CONTRATANTE
    path('contratante/', contratante, name='contratante'),
    path('updatecontratante/<int:pk>/', contratanteEdit, name='contratante_edit'),
    path('deletecontratante/<int:pk>/',
         contratanteDelete, name='contratante_delete'),

    # CONTRATANTE
    path('produtor/', produtor, name='produtor'),
    path('updateprodutor/<int:pk>/', produtorEdit, name='produtor_edit'),
    path('deleteprodutor/<int:pk>/',
         produtorDelete, name='produtor_delete'),

    # MUSICO
    path('musico/', musico, name='musico'),
    path('updatemusico/<int:pk>/', musicoEdit, name='musico_edit'),
    path('deletemusico/<int:pk>/',
         musicoDelete, name='musico_delete'),

    # TECNICO
    path('tecnico/', tecnico, name='tecnico'),
    path('updatetecnico/<int:pk>/', tecnicoEdit, name='tecnico_edit'),
    path('deletetecnico/<int:pk>/',
         tecnicoDelete, name='tecnico_delete'),

]
