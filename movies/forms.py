from django.core.exceptions import ValidationError
from django import forms
from datetime import date

from .models import Movie, Director, Genre, Actor, Review


class YearField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        current_year = date.today().year
        if not value.isdigit() or not (1900 <= int(value) <= current_year):
            raise ValidationError(f'Invalid year: {value}. Year must be a number between 1900 and {current_year}.')


class MovieForm(forms.ModelForm):
    release_year = YearField(label='Release Year')

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'description', 'release_year', 'duration', 'director']


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'date_of_birth', 'is_alive']

    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get('date_of_birth')
        is_alive = cleaned_data.get('is_alive')


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'date_of_birth', 'is_alive']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
