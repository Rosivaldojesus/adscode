# Generated by Django 3.0 on 2020-11-11 20:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesafiosPy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('desafioPython', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Desafio')),
                ('respostaPython', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Resposta')),
            ],
            options={
                'verbose_name_plural': 'Desafios Python',
                'db_table': 'tbDesafiosPy',
            },
        ),
        migrations.AddField(
            model_name='desafiospython',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Título'),
        ),
    ]
