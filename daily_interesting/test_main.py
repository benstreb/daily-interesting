"""Test cases for the base site
"""

from django.core.urlresolvers import reverse
from django.template import loader

from . import views
from .testing import parse_html


def test_base_template(rf):
    request = rf.get("/")
    template = loader.get_template("daily_interesting/base.html")
    template.render({}, request)


def test_index_view(client):
    response = client.get("/")
    html = parse_html(response.content)
    index_element = html.find("a", href=reverse("wiki:index"))
    assert index_element
    assert index_element.string == "Wiki"
    assert response.status_code == 200


def test_get_app_roots():
    roots = views.IndexView.get_app_roots()
    assert ("Wiki", reverse("wiki:index")) in roots
