# Generated by Django 4.2 on 2023-05-02 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='job',
        ),
    ]