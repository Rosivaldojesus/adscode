from django.urls import path

from .views import index
from .views import Css
from .views import Django, DjangoView
from .views import Heroku
from .views import Javascript
from .views import Html
from .views import Library
from .views import Python


urlpatterns = [
    path('', index),

    path('css/', Css),

    path('django/', Django),
    path('djangoView/', DjangoView),

    path('heroku/', Heroku),

    path('javascript/', Javascript),

    path('html/', Html),

    path('library/', Library),

    path('python/', Python),
]