from django import forms
from .models import Movie, Person, Genre, Review, Award, MovieAward
from .widgets import StarRatingWidget


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_year', 'duration', 'genre', 'director']


class PersonForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('actor', 'Actor'),
        ('director', 'Director'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Role")

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date', 'death_date']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(widget=StarRatingWidget())

    class Meta:
        model = Review
        fields = ['movie', 'rating', 'comment']


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['name', 'year_awarded']


class MovieAwardForm(forms.ModelForm):
    class Meta:
        model = MovieAward
        fields = ['movie', 'award', 'category']
