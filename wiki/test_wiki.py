import pytest
from django.core.urlresolvers import reverse

from daily_interesting.testing import parse_html
from . import models, forms


@pytest.fixture
def index_url():
    return reverse("wiki:index")


@pytest.fixture
def new_page_url():
    return reverse("wiki:new_page")


@pytest.fixture
@pytest.mark.django_db
def pages():
    page = models.Page.objects.create(title="Test Title", anchor="anchor", body="Body")
    return [page]


@pytest.mark.django_db
def test_pages(pages):
    assert list(models.Page.objects.filter(title="Test Title", anchor="anchor", body="Body")) == pages


@pytest.mark.django_db
def test_index(client, pages):
    test_page = pages[0]
    response = client.get("/wiki/")
    assert response.status_code == 200
    html = parse_html(response.content)
    anchor = html.find("a", href=reverse("wiki:page", args=[test_page.anchor]))
    assert anchor
    assert anchor.string == test_page.title


@pytest.mark.django_db
def test_index_links_to_page(client, index_url, new_page_url):
    response = client.get(index_url)
    html = parse_html(response.content)
    assert html.find("a", href=new_page_url)


@pytest.mark.django_db
def test_new_page_view(client, new_page_url):
    new_page_data = {
        "title": "test_new_page_view",
        "anchor": "anchor",
        "body": "Body",
    }
    response = client.get(new_page_url)
    assert response.status_code == 200
    html = parse_html(response.content)
    assert html.find("input", type="submit")
    assert html.find("input", type="hidden", attrs={"name": "csrfmiddlewaretoken"})
    post_response = client.post(new_page_url, new_page_data)
    assert models.Page.objects.filter(title="test_new_page_view").count()
    assert post_response.status_code == 302


@pytest.mark.django_db
def test_page_view(client, pages):
    test_page = pages[0]
    response = client.get(reverse("wiki:page", args=[test_page.anchor]))
    assert response.status_code == 200
    html = parse_html(response.content)
    assert html.find("div", class_="container")
    assert html.find("title").string == test_page.title
    assert html.find(id="page-title").string.strip() == test_page.title


@pytest.mark.django_db
def test_page_form():
    form = forms.PageForm({"title": "Title", "anchor": "anchor", "body": "Body"})
    assert form.is_valid()
