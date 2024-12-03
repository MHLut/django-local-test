from django.urls import include, path

from mysite.library.views import (
    CodeSnippetCreateView,
    CodeSnippetDeleteView,
    CodeSnippetDetailView,
    CodeSnippetListView,
    CodeSnippetUpdateView,
)


CODE_SNIPPET_PATHS = [
    path("<int:pk>/delete/", CodeSnippetDeleteView.as_view(), name="code_snippet_delete"),
    path("<int:pk>/update/", CodeSnippetUpdateView.as_view(), name="code_snippet_update"),
    path("<int:pk>/", CodeSnippetDetailView.as_view(), name="code_snippet_detail"),
    path("create/", CodeSnippetCreateView.as_view(), name="code_snippet_create"),
    path("", CodeSnippetListView.as_view(), name="code_snippet_list"),
]


app_name = "library"
urlpatterns = [
    path("code-snippets/", include(CODE_SNIPPET_PATHS)),
]
