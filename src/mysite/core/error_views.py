import pprint
from http import HTTPStatus

from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.http import Http404
from django.shortcuts import render


pp = pprint.PrettyPrinter(indent=2)


def raise_error(request, http_status: int):
    """Raise an error with a given HTTP status code."""
    status_exceptions = {
        HTTPStatus.BAD_REQUEST: SuspiciousOperation,
        HTTPStatus.FORBIDDEN: PermissionDenied,
        HTTPStatus.NOT_FOUND: Http404,
        HTTPStatus.INTERNAL_SERVER_ERROR: RuntimeError,
    }

    if http_status in status_exceptions:
        msg = f"This is a test for HTTP {http_status}."
        raise status_exceptions[http_status](msg)

    raise Http404


def http_400_bad_request_view(request, exception=None, **kwargs):
    """Handle the HTTP 400 Bad Request error."""
    print("-" * 60)
    pp.pprint(exception)
    pp.pprint(kwargs)
    print("-" * 60)
    return render(
        request=request,
        template_name="core/errors/400.html",
        status=400,
    )


def http_403_forbidden_view(request, exception=None, **kwargs):
    """Handle the HTTP 403 Forbidden error."""
    print("-" * 60)
    pp.pprint(exception)
    pp.pprint(kwargs)
    print("-" * 60)
    return render(
        request=request,
        template_name="core/errors/403.html",
        status=403,
    )


def http_404_not_found_view(request, exception=None, **kwargs):
    """Handle the HTTP 404 Not Found error."""
    print("-" * 60)
    pp.pprint(exception)
    pp.pprint(kwargs)
    print("-" * 60)
    return render(
        request=request,
        template_name="core/errors/404.html",
        status=404,
    )


def http_500_internal_server_error_view(request, **kwargs):
    """Handle the HTTP 500 Internal Server Error error."""
    print("-" * 60)
    pp.pprint(kwargs)
    print("-" * 60)
    return render(
        request=request,
        template_name="core/errors/500.html",
        status=500,
    )
