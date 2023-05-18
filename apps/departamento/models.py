from django.db import models


# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    short_name = models.CharField(max_length=20, verbose_name='Nombre corto')
    anulate = models.BooleanField(verbose_name='Anulado', default=False)

    class Meta:
        verbose_name = 'Departamento',
        verbose_name_plural = 'Departamentos'
        ordering = ['-nombre']
        unique_together = ('nombre', 'short_name')

    def __str__(self):
        return '%s - %s' % (self.nombre, self.short_name)
