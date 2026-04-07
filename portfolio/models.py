from django.db import models


class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='making_of/', blank=True, null=True)
    data_registo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Making Of'
        verbose_name_plural = 'Making Of'
        ordering = ['-data_registo']


class TFC(models.Model):
    titulo = models.CharField(max_length=500)
    autor = models.CharField(max_length=300)
    orientador = models.CharField(max_length=300, blank=True)
    licenciatura_nome = models.CharField(max_length=300, blank=True)
    ano = models.IntegerField()
    email = models.EmailField(blank=True)
    url_pdf = models.URLField(max_length=500, blank=True, null=True)
    url_imagem = models.URLField(max_length=500, blank=True, null=True)
    resumo = models.TextField(blank=True)
    classificacao = models.IntegerField(default=3)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'TFC'
        verbose_name_plural = 'TFCs'
        ordering = ['-ano']


class UnidadeCurricular(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=300)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    duracao = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Unidade Curricular'
        verbose_name_plural = 'Unidades Curriculares'
        ordering = ['ano_curricular', 'semestre']
