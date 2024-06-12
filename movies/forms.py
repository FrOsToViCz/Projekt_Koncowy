from django import forms
from .models import Movie, Genre, Person, Cast, Award, MovieAward


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_year', 'duration_minutes', 'genre', 'directors']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date', 'death_date', 'role']


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = ['movie', 'person', 'role_name']


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['name']


class MovieAwardForm(forms.ModelForm):
    class Meta:
        model = MovieAward
        fields = ['movie', 'award', 'category']
