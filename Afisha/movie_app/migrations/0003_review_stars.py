# Generated by Django 5.0.2 on 2024-02-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_movie_director_alter_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10, null=True),
        ),
    ]
