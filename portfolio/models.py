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
    titulo = models.CharField(max_length=300)
    resumo = models.TextField()
    autor = models.CharField(max_length=200)
    ano = models.IntegerField()
    area = models.CharField(max_length=100)
    classificacao = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    url_repositorio = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'TFC'
        verbose_name_plural = 'TFCs'
        ordering = ['-ano']
