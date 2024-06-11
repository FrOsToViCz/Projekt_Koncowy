from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie, Person, Genre, Review, Award, MovieAward, Role
from .forms import MovieForm, PersonForm, GenreForm, ReviewForm, AwardForm, MovieAwardForm


# Widok główny
class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'


# Widok szczegółowy filmu
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


# Widok tworzenia filmu
class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')


# Widok aktualizacji filmu
class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')


# Widok usuwania filmu
class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


# Widok szczegółowy osoby
class PersonDetailView(DetailView):
    model = Person
    template_name = 'movies/person_detail.html'
    context_object_name = 'person'


# Widok tworzenia osoby
class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'movies/person_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        role = form.cleaned_data.get('role')
        if role:
            Role.objects.create(person=self.object, role=role)
        return response

    def get_success_url(self):
        role = self.request.POST.get('role')
        if role == 'actor':
            return reverse_lazy('actor_list')
        elif role == 'director':
            return reverse_lazy('director_list')
        return super().get_success_url()


# Widok aktualizacji osoby
class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'movies/person_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        role = form.cleaned_data.get('role')
        if role:
            Role.objects.update_or_create(person=self.object, defaults={'role': role})
        return response

    def get_success_url(self):
        role = self.request.POST.get('role')
        if role == 'actor':
            return reverse_lazy('actor_list')
        elif role == 'director':
            return reverse_lazy('director_list')
        return super().get_success_url()


# Widok usuwania osoby
class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'movies/person_confirm_delete.html'

    def get_success_url(self):
        role = self.object.role_set.first().role if self.object.role_set.exists() else None
        if role == 'actor':
            return reverse_lazy('actor_list')
        elif role == 'director':
            return reverse_lazy('director_list')
        return super().get_success_url()


# Widok listy aktorów
class ActorListView(ListView):
    model = Person
    template_name = 'movies/actor_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        return Person.objects.filter(role__role='actor').distinct()


# Widok listy reżyserów
class DirectorListView(ListView):
    model = Person
    template_name = 'movies/director_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        return Person.objects.filter(role__role='director').distinct()


# Widok listy gatunków
class GenreListView(ListView):
    model = Genre
    template_name = 'movies/genre_list.html'
    context_object_name = 'genres'


# Widok tworzenia gatunku
class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')


# Widok aktualizacji gatunku
class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')


# Widok usuwania gatunku
class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'movies/genre_confirm_delete.html'
    success_url = reverse_lazy('genre_list')


# Widok tworzenia recenzji
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movies/review_form.html'
    success_url = reverse_lazy('movie_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Widok aktualizacji recenzji
class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movies/review_form.html'
    success_url = reverse_lazy('movie_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Widok usuwania recenzji
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'movies/review_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


# Widok tworzenia nagrody
class AwardCreateView(CreateView):
    model = Award
    form_class = AwardForm
    template_name = 'movies/award_form.html'
    success_url = reverse_lazy('award_list')


# Widok aktualizacji nagrody
class AwardUpdateView(UpdateView):
    model = Award
    form_class = AwardForm
    template_name = 'movies/award_form.html'
    success_url = reverse_lazy('award_list')


# Widok usuwania nagrody
class AwardDeleteView(LoginRequiredMixin, DeleteView):
    model = Award
    template_name = 'movies/award_confirm_delete.html'
    success_url = reverse_lazy('award_list')


# Widok tworzenia nagrody filmowej
class MovieAwardCreateView(CreateView):
    model = MovieAward
    form_class = MovieAwardForm
    template_name = 'movies/movie_award_form.html'
    success_url = reverse_lazy('movie_list')


# Widok aktualizacji nagrody filmowej
class MovieAwardUpdateView(UpdateView):
    model = MovieAward
    form_class = MovieAwardForm
    template_name = 'movies/movie_award_form.html'
    success_url = reverse_lazy('movie_list')


# Widok usuwania nagrody filmowej
class MovieAwardDeleteView(LoginRequiredMixin, DeleteView):
    model = MovieAward
    template_name = 'movies/movie_award_confirm_delete.html'
    success_url = reverse_lazy('movie_list')
