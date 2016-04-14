"""Test cases for the base site
"""

import pytest
from django.core.urlresolvers import reverse
from django.template import loader

from . import views


def test_base_template(rf):
    request = rf.get("/")
    template = loader.get_template("daily_interesting/base.html")
    template.render({}, request)


@pytest.mark.skip
def test_index_view(client):
    response = client.get("/")
    assert b"app_roots" in response.content
    assert response.status_code == 200


def test_get_app_roots():
    roots = views.IndexView.get_app_roots()
    assert ("Wiki", reverse("wiki:index")) in roots
