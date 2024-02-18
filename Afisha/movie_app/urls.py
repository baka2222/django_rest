from django.urls import path
from .views import director_list, director, review_list, review, movie, movie_list

urlpatterns = [
    path('api/v1/director_list/', director_list),
    path('api/v1/director/<int:id>/', director),
    path('api/v1/movie_list/', movie_list),
    path('api/v1/movie/<int:id>/', movie),
    path('api/v1/review_list/', review_list),
    path('api/v1/review/<int:id>/', review)
]