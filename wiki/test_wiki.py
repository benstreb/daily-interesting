import pytest
from bs4 import BeautifulSoup
from django.core.urlresolvers import reverse

from . import models, forms


def parse_html(html):
    return BeautifulSoup(html, "html.parser")


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


@pytest.mark.django_db
def test_index_links_to_page(client):
    index_url = reverse("wiki:index")
    new_page_url = reverse("wiki:new_page")
    response = client.get(index_url)
    html = parse_html(response.content)
    assert html.find("a", href=new_page_url)


@pytest.mark.django_db
def test_new_page_view(client):
    new_page_url = reverse("wiki:new_page")
    new_page_data = {
        "title": "test_new_page_view",
        "body": "Body",
    }
    response = client.get(new_page_url)
    assert response.status_code == 200
    html = parse_html(response.content)
    assert html.find("input", type="submit")
    post_response = client.post(new_page_url, new_page_data)
    assert models.Page.objects.filter(title="test_new_page_view").count()
    assert post_response.status_code == 302


def test_page_form():
    form = forms.PageForm({"title": "Title", "body": "Body"})
    assert form.is_valid()
