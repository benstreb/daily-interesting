""" daily_interesting views

Contains umbrella views for the various apps
"""

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "daily_interesting/index.html"

    def get_context_data(self, **kwargs):
        return {"app_roots": []}
