from django.urls import path
from . import views

urlpatterns = [
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('', views.projetos_view),

    path('projeto/<int:id>/', views.projeto_view, name='projeto'),
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/<int:id>/edita/', views.edita_projeto_view, name='edita_projeto'),
    path('projeto/<int:id>/apaga/', views.apaga_projeto_view, name='apaga_projeto'),

    path('tecnologia/<int:id>/', views.tecnologia_view, name='tecnologia'),
    path('tecnologia/novo/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologia/<int:id>/edita/', views.edita_tecnologia_view, name='edita_tecnologia'),
    path('tecnologia/<int:id>/apaga/', views.apaga_tecnologia_view, name='apaga_tecnologia'),

    path('competencia/<int:id>/', views.competencia_view, name='competencia'),
    path('competencia/novo/', views.nova_competencia_view, name='nova_competencia'),
    path('competencia/<int:id>/edita/', views.edita_competencia_view, name='edita_competencia'),
    path('competencia/<int:id>/apaga/', views.apaga_competencia_view, name='apaga_competencia'),

    path('formacao/<int:id>/', views.formacao_view, name='formacao'),
    path('formacao/novo/', views.nova_formacao_view, name='nova_formacao'),
    path('formacao/<int:id>/edita/', views.edita_formacao_view, name='edita_formacao'),
    path('formacao/<int:id>/apaga/', views.apaga_formacao_view, name='apaga_formacao'),
]
