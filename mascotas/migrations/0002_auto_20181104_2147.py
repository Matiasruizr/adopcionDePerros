# Generated by Django 2.1.2 on 2018-11-05 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perros',
            old_name='naza_predominante',
            new_name='raza_predominante',
        ),
        migrations.AlterField(
            model_name='perros',
            name='estado',
            field=models.CharField(choices=[('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='perros',
            name='foto_mascota',
            field=models.ImageField(upload_to='static/img/perros_subidos'),
        ),
    ]
