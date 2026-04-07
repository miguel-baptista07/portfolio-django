from django.contrib import admin
from .models import (
    Licenciatura, Docente, Tecnologia, UnidadeCurricular,
    Projeto, Competencia, Formacao, Certificado,
    MakingOf, TFC,
)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'grau', 'ects', 'duracao_anos']
    search_fields = ['nome', 'sigla', 'grau']
    list_filter = ['grau']


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'url_lusofona']
    search_fields = ['nome', 'email']


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'nivel_interesse']
    search_fields = ['nome', 'categoria', 'descricao']
    list_filter = ['categoria', 'nivel_interesse']


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'ano', 'semestre', 'ects', 'licenciatura']
    search_fields = ['codigo', 'nome']
    list_filter = ['ano', 'semestre', 'licenciatura']
    filter_horizontal = ['docentes']


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'uc', 'data_inicio', 'data_fim']
    search_fields = ['titulo', 'descricao', 'conceitos_aplicados']
    list_filter = ['uc', 'data_inicio']
    filter_horizontal = ['tecnologias']


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel', 'categoria']
    search_fields = ['nome', 'descricao', 'categoria']
    list_filter = ['nivel', 'categoria']
    filter_horizontal = ['tecnologias', 'projetos']


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'instituicao', 'tipo', 'data_inicio', 'data_fim']
    search_fields = ['titulo', 'instituicao', 'tipo']
    list_filter = ['tipo', 'instituicao']


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'formacao', 'url']
    search_fields = ['codigo', 'formacao__titulo']
    list_filter = ['formacao']


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
