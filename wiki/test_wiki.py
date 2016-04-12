import pytest

from . import models


@pytest.mark.django_db
def test_page():
    page = models.Page.objects.create(title="Test", body="Body")
    assert list(models.Page.objects.filter(title="Test", body="Body")) == [page]
