from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    duration = models.IntegerField(help_text= 'duration in minutes')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed_movies')

    def __str__(self):
        return self.title


class Role(models.Model):
    ROLE_CHOICES = [
        ('director', 'Director'),
        ('actor', 'Actor'),
    ]
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    character = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.person} as {self.character} in {self.movie}"


class Award(models.Model):
    name = models.CharField(max_length=100)
    year_awarded = models.IntegerField()

    def __str__(self):
        return self.name


class MovieAward(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.award} for {self.movie} in category {self.category}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review of {self.movie} by {self.user}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s favorite: {self.movie}"


class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_rated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating of {self.movie} by {self.user}"
