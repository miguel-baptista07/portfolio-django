from django.contrib import admin
from .models import MakingOf, TFC


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_registo']
    search_fields = ['titulo', 'descricao']


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'ano', 'area', 'classificacao']
    search_fields = ['titulo', 'autor', 'area']
    list_filter = ['ano', 'area']
