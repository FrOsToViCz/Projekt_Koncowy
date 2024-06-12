from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie, Genre, Person, Cast, Award, MovieAward
from .forms import MovieForm, GenreForm, PersonForm, CastForm, AwardForm, MovieAwardForm


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


class GenreListView(ListView):
    model = Genre
    template_name = 'movies/genre_list.html'
    context_object_name = 'genres'


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'movies/genre_confirm_delete.html'
    success_url = reverse_lazy('genre_list')


class PersonListView(ListView):
    model = Person
    template_name = 'movies/person_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        role = self.request.GET.get('role')
        if role:
            return Person.objects.filter(role__in=[role, 'both'])
        return Person.objects.all()


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'movies/person_form.html'
    success_url = reverse_lazy('person_list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'movies/person_form.html'
    success_url = reverse_lazy('person_list')


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'movies/person_confirm_delete.html'
    success_url = reverse_lazy('person_list')


class CastCreateView(CreateView):
    model = Cast
    form_class = CastForm
    template_name = 'movies/cast_form.html'
    success_url = reverse_lazy('movie_list')


class CastUpdateView(UpdateView):
    model = Cast
    form_class = CastForm
    template_name = 'movies/cast_form.html'
    success_url = reverse_lazy('movie_list')


class CastDeleteView(DeleteView):
    model = Cast
    template_name = 'movies/cast_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


class AwardListView(ListView):
    model = Award
    template_name = 'movies/award_list.html'
    context_object_name = 'awards'


class AwardCreateView(CreateView):
    model = Award
    form_class = AwardForm
    template_name = 'movies/award_form.html'
    success_url = reverse_lazy('award_list')


class AwardUpdateView(UpdateView):
    model = Award
    form_class = AwardForm
    template_name = 'movies/award_form.html'
    success_url = reverse_lazy('award_list')


class AwardDeleteView(DeleteView):
    model = Award
    template_name = 'movies/award_confirm_delete.html'
    success_url = reverse_lazy('award_list')


class MovieAwardCreateView(CreateView):
    model = MovieAward
    form_class = MovieAwardForm
    template_name = 'movies/movieaward_form.html'
    success_url = reverse_lazy('movie_list')


class MovieAwardDeleteView(DeleteView):
    model = MovieAward
    template_name = 'movies/movieaward_confirm_delete.html'
    success_url = reverse_lazy('movie_list')
