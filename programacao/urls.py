from django.urls import path

from .views import index
from .views import Css, CssView
from .views import Django, DjangoView
from .views import Heroku, HerokuView
from .views import Javascript, JavascriptView
from .views import Html, HtmlView
from .views import Library, LibraryView
from .views import Python, PythonView


urlpatterns = [
    path('', index),

    path('css/', Css),
    path('cssView/', CssView),

    path('django/', Django),
    path('djangoView/', DjangoView),

    path('heroku/', Heroku),
    path('herokuView/', HerokuView),

    path('javascript/', Javascript),
    path('javascriptView/',JavascriptView),

    path('html/', Html),
    path('htmlView/', HtmlView),

    path('library/', Library),
    path('libraryView/', LibraryView),

    path('python/', Python),
    path('pythonView/', PythonView),
]