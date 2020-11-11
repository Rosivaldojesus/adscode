from django.urls import path
from .views import *

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