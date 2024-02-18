from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, RewievSerializer
from .models import Director, Movie, Review

#Режиссеры
@api_view(['GET'])
def director_list(request):
    item = Director.objects.all()
    data = DirectorSerializer(item, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director(request, id):
    item = Director.objects.get(id=id)
    data = DirectorSerializer(item).data
    return Response(data=data)

#Фильмы
@api_view(['GET'])
def movie_list(request):
    item = Movie.objects.all()
    data = MovieSerializer(item, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie(request, id):
    item = Movie.objects.get(id=id)
    data = MovieSerializer(item).data
    return Response(data=data)


@api_view(['GET'])
def review_list(request):
    item = Review.objects.all()
    data = RewievSerializer(item, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review(request, id):
    item = Review.objects.get(id=id)
    data = RewievSerializer(item).data
    return Response(data=data)