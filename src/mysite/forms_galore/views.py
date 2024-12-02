from django.views.generic import FormView

from mysite.forms_galore.forms import SampleForm


class SampleFormView(FormView):
    """Form view displaying the non-functional `SampleForm`."""

    form_class = SampleForm
    template_name = "forms_galore/sample_form/index.html"
