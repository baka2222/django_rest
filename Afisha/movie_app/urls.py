from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/directors/', views.Directors.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetail.as_view()),
    path('api/v1/movies/', views.Movies.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetail.as_view()),
    path('api/v1/reviews/', views.Reviews.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetail.as_view()),
    path('api/v1/auth/login/', views.Login.as_view()),
    path('api/v1/auth/registration/', views.Register.as_view())
]