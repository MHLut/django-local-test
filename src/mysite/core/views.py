from typing import Any

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Website home view (index)."""

    template_name = "core/pages/home/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:  # noqa: D102
        context = super().get_context_data(**kwargs)
        context["http_error_codes"] = [400, 403, 404, 500]
        return context


class KitchenSinkView(TemplateView):
    """HTML element showcase view (kitchen sink)."""

    template_name = "core/pages/kitchen-sink/index.html"
