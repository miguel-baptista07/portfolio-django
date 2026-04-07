from django.contrib import admin
from .models import (
    Licenciatura, Docente, Tecnologia, Projeto,
    Competencia, Formacao, Certificado,
    UnidadeCurricular, TFC, MakingOf,
)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'url']
    search_fields = ['nome', 'sigla']


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'url']
    search_fields = ['nome', 'email']


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'url']
    search_fields = ['nome']


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano', 'url']
    search_fields = ['titulo', 'descricao']
    list_filter = ['ano']
    filter_horizontal = ['tecnologias']


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel']
    search_fields = ['nome', 'descricao']
    list_filter = ['nivel']


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'instituicao', 'ano']
    search_fields = ['titulo', 'instituicao']
    list_filter = ['ano', 'instituicao']


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'instituicao', 'ano']
    search_fields = ['titulo', 'instituicao']
    list_filter = ['ano', 'instituicao']


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'ano_curricular', 'semestre', 'ects']
    search_fields = ['codigo', 'nome']
    list_filter = ['ano_curricular', 'semestre']


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'ano', 'licenciatura_nome', 'classificacao']
    search_fields = ['titulo', 'autor', 'licenciatura_nome']
    list_filter = ['ano', 'licenciatura_nome']


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'entidade_relacionada', 'data_registo']
    list_filter = ['entidade_relacionada', 'data_registo']
    search_fields = ['titulo', 'descricao', 'entidade_relacionada']
    ordering = ['entidade_relacionada', 'data_registo']
