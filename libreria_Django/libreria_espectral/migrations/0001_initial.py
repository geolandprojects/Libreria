# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_captura', models.DateField()),
                ('hora_captura', models.TimeField()),
                ('estado_desarrollo', models.CharField(max_length=45)),
                ('altura_individuo', models.CharField(max_length=45)),
                ('altura_instrumental', models.CharField(max_length=45)),
                ('estado_tiempo', models.CharField(max_length=45)),
                ('imagen_individuo', models.ImageField(upload_to='individuo/')),
                ('imagen_cielo', models.ImageField(upload_to='cielo/')),
                ('imagen_panorama', models.ImageField(upload_to='panorama/')),
            ],
        ),
        migrations.CreateModel(
            name='Firma_Espectral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitud_onda', models.IntegerField(default=0)),
                ('firma', models.DecimalField(decimal_places=16, max_digits=18)),
                ('evento', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libreria_espectral.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cientifico', models.CharField(max_length=200)),
                ('reino', models.CharField(max_length=200)),
                ('filo', models.CharField(max_length=200)),
                ('clase', models.CharField(max_length=200)),
                ('orden', models.CharField(max_length=200)),
                ('familia', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('epiteto_especifico', models.CharField(max_length=200)),
                ('autoria_nombre_cientifico', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=45)),
                ('departamento', models.CharField(max_length=45)),
                ('municipio', models.CharField(max_length=45)),
                ('localidad', models.CharField(max_length=45)),
                ('elevacion', models.FloatField()),
                ('comentario_ubicacion', models.CharField(max_length=200)),
                ('codigo_pais', models.CharField(max_length=45)),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('evento', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libreria_espectral.Evento')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='taxon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria_espectral.Taxon'),
        ),
    ]
