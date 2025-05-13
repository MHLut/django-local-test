"""Context processors for the entire project."""

from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from django.http import HttpRequest


def current_path_processor(request: "HttpRequest") -> dict[str, Any]:
    """
    Context processor with current path information.

    Contains:

    * `current_path`: The current path without query parameters.
    * `current_path_with_query`: The current with with query parameters.

    If the current path is empty, it defaults to `"/"`.
    """
    current_path = request.path
    current_path_with_query = request.get_full_path()

    return {
        "current_path": current_path or "/",
        "current_path_with_query": current_path_with_query or "/",
    }


def frontend_processor(request: "HttpRequest") -> dict[str, Any]:
    """
    Context processor with random data for the frontend.

    Contains:

    * `rel_external`: Use in the `rel` attribute of `<a>` for external links.
    """
    return {
        "rel_external": "external noopener noreferrer",
    }
