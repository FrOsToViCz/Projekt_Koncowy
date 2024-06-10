from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from movies.forms import MovieForm, DirectorForm, GenreForm, ActorForm, ReviewForm
from movies.models import Movie, Director, Actor, Genre


# Relacje
# Jeden do wielu:
# Reżyser -> Filmy
# Jeden reżyser wiele filmów
#
# Film -> Role
# Jeden film może mieć wiele role (aktorów)
#
# Award -> MovieAward
# Jedna nagroda może być przyznana wielu filmom
#
# Movie -> Award
# Jeden film może mieć wiele nagród
#
# Movie -> Review
# Jeden film może mieć wiele recenzji
#
# Film -> UserRating
# Jeden film może mieć wiele ocen użytkowników
#
#
# Wiele do wielu:
# User -> Filmy
# Użytkownicy mogą oznaczać wiele filmów jako ulubione, a każdy film może być ulubionym dla wielu użytkowników
# możliwość oznaczenia, czy film został obejrzany.
#
# Movie -> Actor
# Aktorzy mogą grać w wielu filmach, każdy film może mieć wielu aktorów

class MovieListView(View):

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_list.html", {"movies": movies})


class MovieDetailView(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return render(request, "movies/movie_detail.html", {"movie": movie})


class MovieCreateView(LoginRequiredMixin, View):

    def get(self, request):
        form = MovieForm()
        return render(request, "movies/movie_form.html", {"form": form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            form.save()
            return redirect('movie_list')
        return render(request, "movies/movie_form.html", {"form": form})


class MovieUpdateView(LoginRequiredMixin, View):

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(instance=movie)
        return render(request, "movies/movie_form.html", {"form": form})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
        return render(request, "movies/movie_form.html", {"form": form})


class MovieDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return render(request, "movies/movie_delete.html", {"movie": movie})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return redirect('movie_list')


class DirectorListView(View):
    def get(self, request):
        directors = Director.objects.all()
        return render(request, 'movies/director_list.html', {"directors": directors})


class DirectorCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = DirectorForm()
        return render(request, "movies/director_form.html", {"form": form})

    def post(self, request):
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_list')
        return render(request, "movies/director_form.html", {"form": form})


class DirectorUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        form = DirectorForm(instance=director)
        return render(request, "movies/director_form.html", {"form": form})

    def post(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect('director_list')
        return render(request, "movies/director_form.html", {"form": form})


class DirectorDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        return render(request, "movies/director_delete.html", {"director": director})

    def post(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        director.delete()
        return redirect('director_list')


class GenreListView(View):
    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'movies/genre_list.html', {"genres": genres})


class GenreCreateView(LoginRequiredMixin, View):

    def get(self, request):
        form = GenreForm()
        return render(request, "movies/genre_form.html", {"form": form})

    def post(self, request):
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
        return render(request, "movies/genre_form.html", {"form": form})


class GenreUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        form = GenreForm(instance=genre)
        return render(request, "movies/genre_form.html", {"form": form})

    def post(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
        return render(request, "movies/genre_form.html", {"form": form})


class GenreDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        return render(request, "movies/genre_delete.html", {"genre": genre})

    def post(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return redirect('genre_list')


class ActorListView(View):

    def get(self, request):
        actors = Actor.objects.all()
        return render(request, "movies/actor_list.html", {"actors": actors})


class ActorCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ActorForm()
        return render(request, "movies/actor_form.html", {"form": form})

    def post(self, request):
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
        return render(request, "movies/actor_form.html", {"form": form})


class ActorUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        form = ActorForm(instance=actor)
        return render(request, "movies/actor_form.html", {"form": form})

    def post(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
        return render(request, "movies/actor_form.html", {"form": form})


class ActorDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        return render(request, "movies/actor_delete.html", {"actor": actor})

    def post(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        actor.delete()
        return redirect('actor_list')


class ReviewCreateView(LoginRequiredMixin, View):

    def post(self, request, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', pk=movie.pk)
        return render(request, "movies/movie_detail.html", {"form": form, "movie": movie})
