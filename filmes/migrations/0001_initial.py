# Generated by Django 3.2 on 2021-11-03 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('hora_criacao', models.TimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('hora_atualizacao', models.TimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('capa', models.ImageField(upload_to='filmes_capas/')),
                ('duracao', models.TimeField()),
                ('data_lancamento', models.DateTimeField()),
                ('sinopse', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('hora_criacao', models.TimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('hora_atualizacao', models.TimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome_completo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avaliacao', models.FloatField()),
                ('comentario', models.TextField(max_length=2000)),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmes.filme')),
            ],
            options={
                'verbose_name': 'Avaliacao',
                'verbose_name_plural': 'Avaliacoes',
                'ordering': ['id'],
            },
        ),
    ]