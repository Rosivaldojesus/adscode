from django.shortcuts import render
from .models import ArticleDjango, ArticleCss, ArticleHeroku, ArticleJavaScript
from .models import ArticleHtml, ArticleLibrary, ArticlePython

# Create your views here.
def index(request):
    return render(request, 'index.html')
#-----------------------------------------------------------------------
#------------------------> CSS <----------------------------------------
#-----------------------------------------------------------------------
def Css(request):
    post = ArticleCss.objects.all()
    return render(request, 'css.html',{'post': post})

def CssView(request):
    post = request.GET.get('id')
    if post:
        post = ArticleCss.objects.get(id=post)
    return render(request, 'cssView.html', {'post': post})
#-----------------------------------------------------------------------
#------------------------> DJANGO <-------------------------------------
#-----------------------------------------------------------------------
def Django(request):
    post = ArticleDjango.objects.all()
    return render(request, 'django.html', {'post': post})

def DjangoView(request):
    post = request.GET.get('id')
    if post:
        post = ArticleDjango.objects.get(id=post)
    return render(request, 'djangoView.html', {'post': post})
#-----------------------------------------------------------------------
#------------------------> HEROKU <-------------------------------------
#-----------------------------------------------------------------------
def Heroku(request):
    post = ArticleHeroku.objects.all()
    return render(request, 'heroku.html', {'post': post})

def HerokuView(request):
    post = request.GET.get('id')
    if post:
        post = ArticleHeroku.objects.get(id=post)
    return render(request, 'herokuView.html', {'post': post})
#-----------------------------------------------------------------------
#------------------------> JavaScript <---------------------------------
#-----------------------------------------------------------------------
def Javascript(request):
    post = ArticleJavaScript.objects.all()
    return render(request, 'javascript.html',{'post': post})

def JavascriptView(request):
    post = request.GET.get('id')
    if post:
        post = ArticleJavaScript.objects.get(id=post)
    return render(request, 'javascriptView.html', {'post': post})
#-----------------------------------------------------------------------
#------------------------> HTML <---------------------------------------
#-----------------------------------------------------------------------
def Html(request):
    post = ArticleHtml.objects.all()
    return render(request, 'html.html', {'post': post})

def HtmlView(request):
    post = request.GET.get('id')
    if post:
        post = ArticleHtml.objects.get(id=post)
    return render(request, 'htmlView.html', {'post': post})
#-----------------------------------------------------------------------
#------------------------> LIBRARY <------------------------------------
#-----------------------------------------------------------------------
def Library(request):
    post = ArticleLibrary.objects.all()
    return render(request, 'library.html', {'post': post})

def LibraryView(request):
    post = request.GET.get('id')
    if post:
        post = ArticleLibrary.objects.get(id=post)
    return render(request, 'LibraryView.html', {'post': post})
#-----------------------------------------------------------------------
#------------------------> PYTHON <-------------------------------------
#-----------------------------------------------------------------------
def Python(request):
    post = ArticlePython.objects.all()
    return render(request, 'python.html',{'post': post})

def PythonView(request):
    post = request.GET.get('id')
    if post:
        post = ArticlePython.objects.get(id=post)
    return render(request, 'pythonView.html', {'post': post})