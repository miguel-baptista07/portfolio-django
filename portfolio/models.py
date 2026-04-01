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
