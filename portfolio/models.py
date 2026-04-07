from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Licenciatura'
        verbose_name_plural = 'Licenciaturas'
        ordering = ['nome']


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['nome']


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        ordering = ['nome']


class Projeto(models.Model):
    titulo = models.CharField(max_length=300)
    descricao = models.TextField(blank=True)
    ano = models.IntegerField()
    url = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-ano']


class Competencia(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    nivel = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Competência'
        verbose_name_plural = 'Competências'
        ordering = ['nome']


class Formacao(models.Model):
    titulo = models.CharField(max_length=300)
    instituicao = models.CharField(max_length=200)
    ano = models.IntegerField()
    descricao = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Formação'
        verbose_name_plural = 'Formações'
        ordering = ['-ano']


class Certificado(models.Model):
    titulo = models.CharField(max_length=300)
    instituicao = models.CharField(max_length=200)
    ano = models.IntegerField()
    url = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='certificados/', blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'
        ordering = ['-ano']


class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    decisoes_tomadas = models.TextField()
    erros_correcoes = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)
    foto_caderno = models.ImageField(upload_to='makingof/', blank=True, null=True)
    data_registo = models.DateField(auto_now_add=True)
    entidade_relacionada = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Making Of'
        verbose_name_plural = 'Making Of'
        ordering = ['entidade_relacionada', 'data_registo']


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
