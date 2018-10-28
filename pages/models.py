from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Page(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=100)
    content = RichTextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='orden', default=0)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de Edicion', auto_now=True)

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


