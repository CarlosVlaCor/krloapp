# Generated by Django 4.2 on 2023-05-15 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_habilidades_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre completo'),
        ),
    ]
