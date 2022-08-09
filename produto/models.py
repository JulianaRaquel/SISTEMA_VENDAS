from django.db import models
from django.utils.safestring import mark_safe

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField(default=0)
    descricao = models.TextField()
    img = models.ImageField(upload_to='post_img')
    slug = models.SlugField(unique=True, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="{self.img.url}">'

    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


