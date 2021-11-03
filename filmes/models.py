from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    hora_criacao = models.TimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    hora_atualizacao = models.TimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Filme(Base):
    nome = models.CharField(max_length=255, unique=True)
    capa = models.ImageField(upload_to='filmes_capas/')
    duracao = models.TimeField()
    data_lancamento = models.DateTimeField()
    sinopse = models.TextField(max_length=2000)

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['id']

    def __str__(self):
        return self.nome


class Avaliacao(Base):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    avaliacao = models.FloatField()
    comentario = models.TextField(max_length=2000)

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        ordering = ['id']

    def __str__(self):
        return f'Avaliacao de {str(self.nome_completo)} {str(self.email)}'