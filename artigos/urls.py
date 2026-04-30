from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('<int:artigo_id>/', views.artigo_view, name='artigo'),
    path('novo/', views.novo_artigo_view, name='novo_artigo'),
    path('<int:artigo_id>/editar/', views.edita_artigo_view, name='edita_artigo'),
]
