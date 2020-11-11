# Generated by Django 3.0 on 2020-11-11 21:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles CSS',
                'db_table': 'tbArticleCss',
            },
        ),
        migrations.CreateModel(
            name='ArticleDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles Django',
                'db_table': 'tbArticleDjango',
            },
        ),
        migrations.CreateModel(
            name='ArticleHeroku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles Heroku',
                'db_table': 'tbArticleHeroku',
            },
        ),
        migrations.CreateModel(
            name='ArticleHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles HTML',
                'db_table': 'tbArticleHtml',
            },
        ),
        migrations.CreateModel(
            name='ArticleJavaScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles JavaScript',
                'db_table': 'tbArticleJavaScript',
            },
        ),
        migrations.CreateModel(
            name='ArticleJavaScrit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles JavaScripts',
                'db_table': 'tbArticleJavaScripts',
            },
        ),
        migrations.CreateModel(
            name='ArticleLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles Library',
                'db_table': 'tbArticleLibrary',
            },
        ),
        migrations.CreateModel(
            name='ArticlePython',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('abstract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Articles Python',
                'db_table': 'tbArticlePython',
            },
        ),
        migrations.CreateModel(
            name='DesafiosPython',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=0, max_digits=3)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Título')),
                ('desafio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Desafio')),
                ('resposta', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Resposta')),
            ],
            options={
                'verbose_name_plural': 'Desafios Python',
                'db_table': 'tbDesafiosPython',
            },
        ),
    ]
