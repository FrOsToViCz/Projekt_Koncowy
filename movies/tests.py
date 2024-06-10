from multiprocessing.connection import Client

import pytest
from django.test import TestCase
from django.urls import reverse


@pytest.mark.django_db
def test_base_view():
    url = reverse('base')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
