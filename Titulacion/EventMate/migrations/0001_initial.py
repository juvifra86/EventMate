# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-25 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='califica_usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField(default=0)),
                ('calificacion', models.IntegerField(default=0)),
                ('comentario', models.CharField(default='', max_length=120)),
                ('init', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=60)),
                ('creador_id', models.IntegerField(default=0)),
                ('descripcion', models.CharField(default='', max_length=120)),
                ('Lugar', models.CharField(max_length=120)),
                ('Fecha', models.DateTimeField(default='1900-01-01')),
                ('Precio', models.FloatField(default=0.0)),
                ('stado', models.IntegerField(default=0)),
                ('init', models.DateTimeField(auto_now_add=True)),
                ('finish', models.DateTimeField(default='1900-01-01')),
                ('imagen1', models.FileField(blank=True, null=True, upload_to='evento_img/')),
                ('imagen2', models.FileField(blank=True, null=True, upload_to='evento_img/')),
                ('imagen3', models.FileField(blank=True, null=True, upload_to='evento_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_remitente', models.IntegerField(default=0)),
                ('mensaje', models.CharField(default='', max_length=120)),
                ('stado', models.IntegerField(default=0)),
                ('init', models.DateTimeField(auto_now_add=True)),
                ('finish', models.DateTimeField(default='1900-01-01')),
            ],
        ),
        migrations.CreateModel(
            name='Magazin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField(default=0)),
                ('descripcion', models.CharField(default='', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(default='', max_length=60)),
                ('edad', models.IntegerField(default=0)),
                ('hobbies', models.CharField(default='', max_length=60)),
                ('descripcion', models.CharField(default='', max_length=160)),
                ('email', models.EmailField(default='', max_length=254)),
                ('usuario', models.CharField(default='', max_length=60)),
                ('contrasena', models.CharField(default='', max_length=60)),
                ('respuesta', models.CharField(default='', max_length=60)),
                ('imagen', models.FileField(blank=True, null=True, upload_to='mediaf/')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventMate.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='usuario_evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_evento', models.IntegerField(default=0)),
                ('id_usuario', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='magazin',
            name='Tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventMate.tipo_evento'),
        ),
        migrations.AddField(
            model_name='inbox',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventMate.usuario'),
        ),
        migrations.AddField(
            model_name='evento',
            name='Tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventMate.tipo_evento'),
        ),
    ]
