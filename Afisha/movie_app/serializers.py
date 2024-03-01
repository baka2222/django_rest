from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Director, Movie, Review


class DirectorValidationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=2)

    def validate(self, attrs):
        if not attrs['name']:
            raise ValidationError('Напишите корректное имя директора')


class MovieValidationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=300)
    duration = serializers.CharField(max_length=20)
    director = serializers.CharField(max_length=50)

    def validate(self, attrs):
        try:
            Director.objects.get(name=attrs['director'])
        except:
            raise ValidationError('Нету директора с таким именем')


class ReviewValidationSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    movie = serializers.CharField(max_length=70)
    stars =  serializers.CharField(max_length=10)

    def validate(self, attrs):
        try:
            Movie.objects.get(title=attrs['movie'])
        except:
            raise ValidationError('Нет такого фильма')

        try:
            stars = int(attrs['stars'])
        except:
            raise ValidationError('Вводите число в качестве оценки')
        if stars < 1 or stars > 5:
            raise ValidationError('Оценка должна быть в диопозоне от 1 до 5')


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movie_count(self, director):
        return director.movie.all().count()


class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rating(self, movie):
        try:
            rates = [int(i.stars) for i in movie.reviews.all()]
            return sum(rates)/len(rates)
        except:
            return 'Рейтинга нету'

    def get_reviews(self, movie):
        return RewievSerializer(movie.reviews.all(), many=True).data


class RewievSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()

