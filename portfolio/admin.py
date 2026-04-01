from django.contrib import admin
from .models import MakingOf


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_registo']
    search_fields = ['titulo', 'descricao']
