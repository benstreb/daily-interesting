from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from . import models, forms


class IndexView(ListView):
    template_name = "wiki/index.html"
    queryset = models.Page.objects.all()
    context_object_name = "pages"


class NewPageView(CreateView):
    template_name = "wiki/new_page.html"
    form_class = forms.PageForm
    success_url = reverse_lazy("wiki:index")
