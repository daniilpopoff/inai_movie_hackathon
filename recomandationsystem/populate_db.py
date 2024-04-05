# populate_db.py (в корневой папке вашего Django-проекта)

import csv
from recomandfunc.models import Movie, Rating

def populate_movies(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Movie.objects.create(
                movieId=row['movieId'],
                title=row['title'],
                genres=row['genres']
            )

def populate_ratings(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Rating.objects.create(
                userId=row['userId'],
                movieId_id=row['movieId'],
                rating=row['rating'],
                timestamp=row['timestamp']
            )

# Загрузите данные из датасетов
populate_movies('path_to_movies.csv')
populate_ratings('path_to_ratings.csv')

