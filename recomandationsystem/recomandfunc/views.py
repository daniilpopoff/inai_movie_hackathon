from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Rating, Movie

# def recommend_movies(request):
#     user = request.user  # Получаем текущего пользователя
#
#     # Получаем оценки, которые пользователь поставил фильмам
#     user_ratings = Rating.objects.filter(user=user)
#
#     # Находим средний рейтинг каждого фильма
#     movie_ratings = {}
#     for rating in user_ratings:
#         movie_id = rating.movie.id
#         if movie_id in movie_ratings:
#             movie_ratings[movie_id]['total'] += rating.rating
#             movie_ratings[movie_id]['count'] += 1
#         else:
#             movie_ratings[movie_id] = {'total': rating.rating, 'count': 1}
#
#     # Вычисляем средний рейтинг каждого фильма
#     for movie_id, rating_info in movie_ratings.items():
#         movie_ratings[movie_id]['average'] = rating_info['total'] / rating_info['count']
#
#     # Сортируем фильмы по убыванию среднего рейтинга
#     sorted_movies = sorted(movie_ratings.items(), key=lambda x: x[1]['average'], reverse=True)
#
#     # Получаем рекомендации (просто первые несколько фильмов из отсортированного списка)
#     recommended_movies = [Movie.objects.get(id=movie[0]) for movie in sorted_movies[:5]]
#
#     return render(request, 'recommendations.html', {'movies': recommended_movies})


# views.py (в вашем приложении)

from django.shortcuts import render
from .models import Movie, Rating

def recommend_movies(request, user_id):
    # Получаем рейтинги, оставленные пользователем
    user_ratings = Rating.objects.filter(userId=user_id)

    # Находим других пользователей, чьи оценки похожи на оценки этого пользователя

    # Реализуйте здесь ваш алгоритм рекомендаций на основе рейтингов фильмов

    # Возвращаем список рекомендованных фильмов
    recommended_movies = []

    return render(request, 'recommendations.html', {'movies': recommended_movies})
