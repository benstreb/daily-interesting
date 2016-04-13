import pytest

from . import models


@pytest.fixture
@pytest.mark.django_db
def pages():
    models.Page.objects.create(title="Test Title", body="Body")


@pytest.mark.django_db
def test_page():
    page = models.Page.objects.create(title="Test", body="Body")
    assert list(models.Page.objects.filter(title="Test", body="Body")) == [page]


@pytest.mark.django_db
def test_index(client, pages):
    response = client.get("/wiki/")
    assert response.status_code == 200
    assert b'Test Title' in response.content
