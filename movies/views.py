from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie, Genre, Person, Cast, Award, MovieAward, Review
from .forms import MovieForm, GenreForm, PersonForm, CastForm, AwardForm, MovieAwardForm, ReviewForm


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = self.request.GET.get('q')
        if queryset:
            return Movie.objects.filter(title__icontains=queryset)
        return Movie.objects.all()


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(movie=self.object)
        return context


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


class CastCreateView(LoginRequiredMixin, CreateView):
    model = Cast
    form_class = CastForm
    template_name = 'movies/cast_form.html'
    success_url = reverse_lazy('movie_list')

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.pk})


class CastUpdateView(LoginRequiredMixin, UpdateView):
    model = Cast
    form_class = CastForm
    template_name = 'movies/cast_form.html'
    success_url = reverse_lazy('movie_list')

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.pk})


class CastDeleteView(DeleteView):
    model = Cast
    template_name = 'movies/cast_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.pk})


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
        query = self.request.GET.get('q')
        role = self.request.GET.get('role')
        queryset = Person.objects.all()
        if role:
            if role == 'actor':
                return Person.objects.filter(role__in=['actor', 'both'])
            elif role == 'director':
                return Person.objects.filter(role__in=['director', 'both'])
        if query:
            queryset = queryset.filter(first_name__icontains=query) | queryset.filter(last_name__icontains=query)
        return queryset


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


class PersonDetailView(DetailView):
    model = Person
    template_name = 'movies/person_detail.html'
    context_object_name = 'person'


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


class AwardDetailView(DetailView):
    model = Award
    template_name = 'movies/award_detail.html'
    context_object_name = 'award'


class MovieAwardCreateView(CreateView):
    model = MovieAward
    form_class = MovieAwardForm
    template_name = 'movies/movieaward_form.html'
    success_url = reverse_lazy('movie_list')


class MovieAwardDeleteView(DeleteView):
    model = MovieAward
    template_name = 'movies/movieaward_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


class ReviewListView(ListView):
    model = Review
    template_name = 'movies/review_list.html'
    context_object_name = 'reviews'
    ordering = ['-created_at']


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movies/review_form.html'
    success_url = reverse_lazy('review_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movies/review_form.html'
    success_url = reverse_lazy('review_list')


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'movies/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')
