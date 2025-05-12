from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Website home view (index)."""

    template_name = "core/pages/home/index.html"
