from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя директора")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Названия кино')
    description = models.TextField(max_length=300, verbose_name='Описание')
    duration = models.CharField(max_length=15, verbose_name='Длительность')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='Директор', related_name='movie')

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    text = models.TextField(max_length=300, verbose_name='Комментарий')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='review', related_name='reviews')
    stars = models.CharField(max_length=10, choices=RATING, null=True)

    def __str__(self):
        return self.text
