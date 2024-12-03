from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from mysite.library.models import CodeSnippet


class CodeSnippetBaseView(LoginRequiredMixin):
    """Base data for views for the `CodeSnippet` model."""

    model = CodeSnippet
    context_object_name = "code_snippet"


class CodeSnippetListView(CodeSnippetBaseView, ListView):
    """List view for the `CodeSnippet` model."""

    template_name = "library/code_snippets/list/index.html"
    context_object_name = "code_snippets"


class CodeSnippetCreateView(CodeSnippetBaseView, CreateView):
    """Create view for the `CodeSnippet` model."""

    fields = ("title", "language", "contents")
    template_name = "library/code_snippets/create/index.html"

    def form_valid(self, form):
        """Set the creator to the current user on success."""
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CodeSnippetDetailView(CodeSnippetBaseView, DetailView):
    """Detail view for the `CodeSnippet` model."""

    template_name = "library/code_snippets/detail/index.html"


class CodeSnippetUpdateView(CodeSnippetBaseView, UpdateView):
    """Update view for the `CodeSnippet` model."""

    fields = ("title", "language", "contents")
    template_name = "library/code_snippets/update/index.html"


class CodeSnippetDeleteView(CodeSnippetBaseView, DeleteView):
    """Delete view for the `CodeSnippet` model."""

    template_name = "library/code_snippets/delete/index.html"
