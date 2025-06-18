from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('pagamentos/', views.pagamentos, name='pagamentos'),
    path('dados-pessoais/', views.dados_pessoais, name='dados_pessoais'),
    path('disciplinas/', views.disciplinas, name='disciplinas'),
    path('documentos/', views.documentos, name='documentos'),
    path('notas/', views.notas, name='notas'),
]
