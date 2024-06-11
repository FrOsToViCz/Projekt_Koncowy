from django.urls import path
from django.views.generic import TemplateView

from movies.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
    path('person/new/', PersonCreateView.as_view(), name='person_create'),
    path('person/<int:pk>/edit/', PersonUpdateView.as_view(), name='person_update'),
    path('person/<int:pk>/delete/', PersonDeleteView.as_view(), name='person_delete'),
    path('actors/', ActorListView.as_view(), name='actor_list'),
    path('directors/', DirectorListView.as_view(), name='director_list'),
    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('genres/new/', GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/edit/', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),
    path('review/new/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('award/new/', AwardCreateView.as_view(), name='award_create'),
    path('award/<int:pk>/edit/', AwardUpdateView.as_view(), name='award_update'),
    path('award/<int:pk>/delete/', AwardDeleteView.as_view(), name='award_delete'),
    path('movie_award/new/', MovieAwardCreateView.as_view(), name='movie_award_create'),
    path('movie_award/<int:pk>/edit/', MovieAwardUpdateView.as_view(), name='movie_award_update'),
    path('movie_award/<int:pk>/delete/', MovieAwardDeleteView.as_view(), name='movie_award_delete'),
]
