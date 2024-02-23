from rest_framework import serializers
from .models import Director, Movie, Review


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

