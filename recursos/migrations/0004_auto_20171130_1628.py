# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_actividad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticker', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Documentos',
                'db_table': 'documento',
            },
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('fecha_recepcion', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Ordenes de trabajo',
                'db_table': 'orden_trabajo',
            },
        ),
        migrations.AddField(
            model_name='documento',
            name='orden_trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.OrdenTrabajo'),
        ),
    ]
