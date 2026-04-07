from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20, blank=True)
    grau = models.CharField(max_length=100, blank=True)
    ects = models.IntegerField(null=True, blank=True)
    duracao_anos = models.IntegerField(null=True, blank=True)
    url_lusofona = models.URLField(blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Licenciatura'
        verbose_name_plural = 'Licenciaturas'
        ordering = ['nome']


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    url_lusofona = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['nome']


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url_oficial = models.URLField(blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    nivel_interesse = models.IntegerField(default=3)
    pontos_destaque = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        ordering = ['nome']


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=300)
    codigo = models.CharField(max_length=20, unique=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    licenciatura = models.ForeignKey(
        Licenciatura, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='unidades_curriculares'
    )
    docentes = models.ManyToManyField(Docente, blank=True, related_name='unidades_curriculares')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Unidade Curricular'
        verbose_name_plural = 'Unidades Curriculares'
        ordering = ['ano', 'semestre']


class Projeto(models.Model):
    titulo = models.CharField(max_length=300)
    descricao = models.TextField(blank=True)
    conceitos_aplicados = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    url_github = models.URLField(blank=True)
    url_demo = models.URLField(blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    uc = models.ForeignKey(
        UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='projetos'
    )
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='projetos')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-data_inicio']


class Competencia(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    nivel = models.CharField(max_length=50, blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='competencias')
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='competencias')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Competência'
        verbose_name_plural = 'Competências'
        ordering = ['nome']


class Formacao(models.Model):
    titulo = models.CharField(max_length=300)
    instituicao = models.CharField(max_length=200)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    url_certificado = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Formação'
        verbose_name_plural = 'Formações'
        ordering = ['-data_inicio']


class Certificado(models.Model):
    codigo = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    formacao = models.ForeignKey(
        Formacao, on_delete=models.CASCADE,
        related_name='certificados'
    )

    def __str__(self):
        return self.codigo or f'Certificado #{self.pk}'

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'
        ordering = ['formacao']


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
