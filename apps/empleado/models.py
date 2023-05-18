from django.db import models
from apps.departamento.models import Departamento


class Habilidades(models.Model):
    habilidad = models.CharField(verbose_name='Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return '%s' % self.habilidad


# Create your models here.
class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    first_name = models.CharField(max_length=60, verbose_name='Primer nombre')
    last_name = models.CharField(max_length=60, verbose_name='Apellido')
    job = models.CharField(verbose_name='Trabajo', max_length=1, choices=JOB_CHOICES)
    full_name = models.CharField(verbose_name='Nombre completo',
                                 max_length=120,
                                 blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    # image = models.ImageField

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Mi Empleo'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')