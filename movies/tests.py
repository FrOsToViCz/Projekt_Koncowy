import pytest
from django.test import Client
from django.urls import reverse


def test_base_view():
    url = reverse('base')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_page_view(client):
    url = reverse('base')
    response = client.get(url)
    assert response.status_code == 200
    assert 'main_interface.html' in [t.name for t in response.templates]
    assert 'MOVIES COLLECTION' in response.content.decode()


@pytest.mark.django_db
def test_home_page_view_logged_in(client, user):
    client.force_login(user)
    url = reverse('base')
    response = client.get(url)
    assert response.status_code == 200
    assert 'main_interface.html' in [t.name for t in response.templates]
    assert 'MOVIES COLLECTION' in response.content.decode()
    assert f'Hello {user.username}!' in response.content.decode()


@pytest.mark.django_db
def test_movie_list_view(client, movie):
    url = reverse('movie_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/movie_list.html' in [t.name for t in response.templates]
    assert movie.title in response.content.decode()


@pytest.mark.django_db
def test_movie_detail_view(client, movie):
    url = reverse('movie_detail', kwargs={'pk': movie.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/movie_detail.html' in [t.name for t in response.templates]
    assert movie.title in response.content.decode()


@pytest.mark.django_db
def test_movie_create_view_redirect_if_not_logged_in(client):
    url = reverse('movie_add')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_movie_create_view_logged_in(client, user):
    client.force_login(user)
    url = reverse('movie_add')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/movie_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_movie_update_view_redirect_if_not_logged_in(client, movie):
    url = reverse('movie_edit', kwargs={'pk': movie.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_movie_update_view_logged_in(client, user, movie):
    client.force_login(user)
    url = reverse('movie_edit', kwargs={'pk': movie.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/movie_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_movie_delete_view_redirect_if_not_logged_in(client, movie):
    url = reverse('movie_delete', kwargs={'pk': movie.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_movie_delete_view_logged_in(client, user, movie):
    client.force_login(user)
    url = reverse('movie_delete', kwargs={'pk': movie.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/movie_confirm_delete.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_genre_list_view(client, genre):
    url = reverse('genre_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/genre_list.html' in [t.name for t in response.templates]
    assert genre.name in response.content.decode()


@pytest.mark.django_db
def test_genre_create_view_redirect_if_not_logged_in(client):
    url = reverse('genre_add')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_genre_create_view_logged_in(client, user):
    client.force_login(user)
    url = reverse('genre_add')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/genre_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_genre_update_view_redirect_if_not_logged_in(client, genre):
    url = reverse('genre_edit', kwargs={'pk': genre.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_genre_update_view_logged_in(client, user, genre):
    client.force_login(user)
    url = reverse('genre_edit', kwargs={'pk': genre.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/genre_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_genre_delete_view_redirect_if_not_logged_in(client, genre):
    url = reverse('genre_delete', kwargs={'pk': genre.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_genre_delete_view_logged_in(client, user, genre):
    client.force_login(user)
    url = reverse('genre_delete', kwargs={'pk': genre.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/genre_confirm_delete.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_person_list_view(client, person):
    url = reverse('person_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/person_list.html' in [t.name for t in response.templates]
    assert person.first_name in response.content.decode()


@pytest.mark.django_db
def test_person_detail_view(client, person):
    url = reverse('person_detail', kwargs={'pk': person.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/person_detail.html' in [t.name for t in response.templates]
    assert person.first_name in response.content.decode()


@pytest.mark.django_db
def test_person_create_view_redirect_if_not_logged_in(client):
    url = reverse('person_add')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_person_create_view_logged_in(client, user):
    client.force_login(user)
    url = reverse('person_add')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/person_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_person_update_view_redirect_if_not_logged_in(client, person):
    url = reverse('person_edit', kwargs={'pk': person.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_person_update_view_logged_in(client, user, person):
    client.force_login(user)
    url = reverse('person_edit', kwargs={'pk': person.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/person_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_person_delete_view_redirect_if_not_logged_in(client, person):
    url = reverse('person_delete', kwargs={'pk': person.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_person_delete_view_logged_in(client, user, person):
    client.force_login(user)
    url = reverse('person_delete', kwargs={'pk': person.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/person_confirm_delete.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_review_list_view(client, review):
    url = reverse('review_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/review_list.html' in [t.name for t in response.templates]
    assert review.text in response.content.decode()


@pytest.mark.django_db
def test_review_create_view_redirect_if_not_logged_in(client):
    url = reverse('review_add')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_review_create_view_logged_in(client, user):
    client.force_login(user)
    url = reverse('review_add')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/review_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_review_update_view_redirect_if_not_logged_in(client, review):
    url = reverse('review_edit', kwargs={'pk': review.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_review_update_view_logged_in(client, user, review):
    client.force_login(user)
    url = reverse('review_edit', kwargs={'pk': review.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/review_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_review_delete_view_redirect_if_not_logged_in(client, review):
    url = reverse('review_delete', kwargs={'pk': review.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_review_delete_view_logged_in(client, user, review):
    client.force_login(user)
    url = reverse('review_delete', kwargs={'pk': review.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/review_confirm_delete.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_award_list_view(client, award):
    url = reverse('award_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/award_list.html' in [t.name for t in response.templates]
    assert award.name in response.content.decode()


@pytest.mark.django_db
def test_award_create_view_redirect_if_not_logged_in(client):
    url = reverse('award_add')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_award_create_view_logged_in(client, user):
    client.force_login(user)
    url = reverse('award_add')
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/award_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_award_update_view_redirect_if_not_logged_in(client, award):
    url = reverse('award_edit', kwargs={'pk': award.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_award_update_view_logged_in(client, user, award):
    client.force_login(user)
    url = reverse('award_edit', kwargs={'pk': award.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/award_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_award_delete_view_redirect_if_not_logged_in(client, award):
    url = reverse('award_delete', kwargs={'pk': award.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_award_delete_view_logged_in(client, user, award):
    client.force_login(user)
    url = reverse('award_delete', kwargs={'pk': award.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/award_confirm_delete.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_movie_award_create_view_redirect_if_not_logged_in(client, movie):
    url = reverse('movie_award_add') + f'?movie={movie.pk}'
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_movie_award_create_view_logged_in(client, user, movie):
    client.force_login(user)
    url = reverse('movie_award_add') + f'?movie={movie.pk}'
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/movieaward_form.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_movie_award_delete_view_redirect_if_not_logged_in(client, movie_award):
    url = reverse('movie_award_delete', kwargs={'pk': movie_award.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')


@pytest.mark.django_db
def test_movie_award_delete_view_logged_in(client, user, movie_award):
    client.force_login(user)
    url = reverse('movie_award_delete', kwargs={'pk': movie_award.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'movies/movieaward_confirm_delete.html' in [t.name for t in response.templates]
