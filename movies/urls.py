"""
URL configuration for ProjektKoncowy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from movies.views import *

urlpatterns = [
    path('movie/list', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('directors/', DirectorListView.as_view(), name='director_list'),
    path('directors/new/', DirectorCreateView.as_view(), name='director_create'),
    path('directors/<int:pk>/edit/', DirectorUpdateView.as_view(), name='director_update'),
    path('directors/<int:pk>/delete/', DirectorDeleteView.as_view(), name='director_delete'),
    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('genres/new/', GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/edit/', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),
    path('actors/', ActorListView.as_view(), name='actor_list'),
    path('actors/new/', ActorCreateView.as_view(), name='actor_create'),
    path('actors/<int:pk>/edit/', ActorUpdateView.as_view(), name='actor_update'),
    path('actors/<int:pk>/delete/', ActorDeleteView.as_view(), name='actor_delete'),
    path('movie/<int:movie_pk>/review/', ReviewCreateView.as_view(), name='review_create'),
]
