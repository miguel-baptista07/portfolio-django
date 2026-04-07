from django.contrib import admin
from .models import MakingOf, TFC


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'entidade_relacionada', 'data_registo']
    list_filter = ['entidade_relacionada', 'data_registo']
    search_fields = ['titulo', 'descricao', 'entidade_relacionada']
    ordering = ['entidade_relacionada', 'data_registo']


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'ano', 'licenciatura_nome', 'classificacao']
    search_fields = ['titulo', 'autor', 'licenciatura_nome']
    list_filter = ['ano', 'licenciatura_nome']
