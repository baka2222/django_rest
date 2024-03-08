from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (DirectorValidationSerializer,
                          MovieValidationSerializer,
                          ReviewValidationSerializer)
from .models import Director, Movie, Review
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)


#Ауторизация
class Login(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                try:
                    tkn = Token.objects.get(user=user)
                except Token.DoesNotExist:
                    tkn = Token.objects.create(user=user)
                return Response(data={'message': tkn.key}, status=status.HTTP_200_OK)
            else:
                return Response(data={'message': 'Ошибка'}, status=status.HTTP_404_NOT_FOUND)


class Register(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            email_ = request.data['email']
            try:
                User.objects.create_user(username=username, password=password, email=email_)
            except:
                return Response(data={'message': 'ошибка'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data={'message': 'Успешно. Авторизируйтесь',
                                  'link_for_signup': 'api/v1/login'},
                            status=status.HTTP_201_CREATED)


#Режиссеры
class Directors(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorValidationSerializer


class DirectorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorValidationSerializer
    lookup_field = 'id'


#Фильмы
class Movies(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieValidationSerializer


class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieValidationSerializer
    lookup_field = 'id'


#Комментарии
class Reviews(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewValidationSerializer


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewValidationSerializer
    lookup_field = 'id'
