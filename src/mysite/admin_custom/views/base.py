from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import ContextMixin, View


class CustomAdminBaseView(ContextMixin, View):
    """Base view for custom admin pages."""

    @classmethod
    def as_view(cls, *args, **kwargs):
        """Apply `staff_member_required` decorator to the view."""
        view = super().as_view(*args, **kwargs)
        return staff_member_required(view)

    def get_context_data(self, **kwargs):  # noqa: D102
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "title": None,
            "subtitle": None,
        }
