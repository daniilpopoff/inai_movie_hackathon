# urls.py

from django.urls import path
from .views import recommend_movies

urlpatterns = [
    path('recommendations/', recommend_movies, name='recommend_movies'),
]
