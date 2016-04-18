""" wiki url configuration
"""

from django.conf.urls import url

from . import views

app_name = "wiki"
urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^new$", views.NewPageView.as_view(), name="new_page"),
    url(r"^page/(?P<slug>[-\w]+)$", views.PageView.as_view(), name="page"),
]
