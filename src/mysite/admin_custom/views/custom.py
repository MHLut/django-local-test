from typing import ClassVar

from django.utils.translation import pgettext_lazy
from django.views.generic import TemplateView

from mysite.admin_custom.views.base import CustomAdminBaseView


class ZenOfPythonAdminView(CustomAdminBaseView, TemplateView):
    """Custom admin page showing the Zen of Python (PEP 20)."""

    template_name = "admin/admin_custom/zen_of_python/index.html"

    APHORISMS: ClassVar = [
        pgettext_lazy(
            "Zen of Python aphorism 01",
            "Beautiful is better than ugly.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 02",
            "Explicit is better than implicit.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 03",
            "Simple is better than complex.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 04",
            "Complex is better than complicated.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 05",
            "Flat is better than nested.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 06",
            "Sparse is better than dense.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 07",
            "Readability counts.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 08",
            "Special cases aren't special enough to break the rules.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 09",
            "Although practicality beats purity.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 10",
            "Errors should never pass silently.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 11",
            "Unless explicitly silenced.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 12",
            "In the face of ambiguity, refuse the temptation to guess.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 13",
            "There should be one-- and preferably only one --obvious way to do it.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 14",
            "Although that way may not be obvious at first unless you're Dutch.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 15",
            "Now is better than never.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 16",
            "Although never is often better than *right* now.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 17",
            "If the implementation is hard to explain, it's a bad idea.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 18",
            "If the implementation is easy to explain, it may be a good idea.",
        ),
        pgettext_lazy(
            "Zen of Python aphorism 19",
            "Namespaces are one honking great idea -- let's do more of those!",
        ),
    ]

    def get_context_data(self, **kwargs):  # noqa: D102
        return {
            **super().get_context_data(**kwargs),
            "title": pgettext_lazy(
                "Admin page title, Zen of Python",
                "Zen of Python",
            ),
            "aphorisms": self.APHORISMS,
        }
