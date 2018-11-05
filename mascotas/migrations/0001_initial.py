# Generated by Django 2.1.2 on 2018-11-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(max_length=200)),
                ('naza_predominante', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=2000)),
                ('foto_mascota', models.ImageField(upload_to='photo')),
                ('estado', models.CharField(max_length=200)),
            ],
        ),
    ]