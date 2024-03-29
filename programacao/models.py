from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class ArticleCss(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticleCss'
        verbose_name_plural = 'Articles CSS'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)



class ArticleDjango(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticleDjango'
        verbose_name_plural = 'Articles Django'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)



class ArticleHeroku(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticleHeroku'
        verbose_name_plural = 'Articles Heroku'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)



class ArticleJavaScrit(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticleJavaScripts'
        verbose_name_plural = 'Articles JavaScripts'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)


class ArticleJavaScript(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticleJavaScript'
        verbose_name_plural = 'Articles JavaScript'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)





class ArticleHtml(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticleHtml'
        verbose_name_plural = 'Articles HTML'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)



class ArticleLibrary(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticleLibrary'
        verbose_name_plural = 'Articles Library'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)


class ArticlePython(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título")
    abstract = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(blank=True, null=True, verbose_name="Texto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbArticlePython'
        verbose_name_plural = 'Articles Python'

    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.created_at)


class ExerciciosBasicosPy(models.Model):
    numero = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    exercicio = RichTextField(blank=True, null=True, verbose_name="Exercício")
    resposta = RichTextField(blank=True, null=True, verbose_name="Resposta")

    class Meta:
        db_table = "ExerciciosBasicosPy"
        verbose_name_plural = 'Exercicios Basicos PY'

    def __str__(self):
        return "{} - {}".format(self.numero, self.exercicio)







