from django.views.generic import ListView

from . import models


class IndexView(ListView):
    template_name = "wiki/index.html"
    queryset = models.Page.objects.all()
    context_object_name = "pages"
