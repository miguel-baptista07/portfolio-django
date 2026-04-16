from django.contrib import admin
from .models import Aluno, Professor, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('alunos',)


admin.site.register(Aluno)
admin.site.register(Professor)
