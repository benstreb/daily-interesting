"""Test cases for the base site
"""

from django.core.urlresolvers import reverse

from . import views


def test_index_view(client):
    response = client.get("/")
    assert "app_roots" in response.context
    assert response.status_code == 200


def test_get_app_roots():
    roots = views.IndexView.get_app_roots()
    assert ("Wiki", reverse("wiki:index")) in roots
