from django.forms import ModelForm

from . import models


class PageForm(ModelForm):
    class Meta:
        model = models.Page
        exclude = []
