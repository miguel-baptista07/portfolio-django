from django.db import models


class Professor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='cursos/')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    alunos = models.ManyToManyField(Aluno, related_name='cursos')

    def __str__(self):
        return self.nome
