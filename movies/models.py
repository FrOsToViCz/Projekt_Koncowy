from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        status = ''
        if not self.is_alive:
            status = '(dead)'
        return f'{self.first_name} {self.last_name}{status}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(help_text='Duration in minutes')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        status = ''
        if not self.is_alive:
            status = '(dead)'
        return f'{self.first_name} {self.last_name}{status}'


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.actor} as {self.character_name}" in f"{self.movie}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.movie}"


class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.TextField('* ')
    comment = models.TextField(blank=True, null=True)
    rated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} rated {self.movie} {self.rating} stars"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} favorite {self.movie}"


class Award(models.Model):
    name = models.CharField(max_length=100)
    award_date = models.DateField()

    def __str__(self):
        return self.name


class MovieAward(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.movie} won {self.award} for {self.category}"
