from django import forms
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SampleForm(forms.Form):
    """Form containing a collection of different fields."""

    class BoolChoices(TextChoices):
        YES = "y", _("Yes")
        NO = "n", _("No")

    required = forms.CharField(
        label=_("Required"), help_text=_("Leave this field empty to trigger an error.")
    )
    disabled = forms.CharField(label=_("Disabled"), disabled=True, required=False)
    integer = forms.IntegerField(label=_("Integer (number input)"), required=False)
    # Numeric text input instead of a number input:
    # https://technology.blog.gov.uk/2020/02/24/why-the-gov-uk-design-system-team-changed-the-input-type-for-numbers/
    integer_as_text = forms.IntegerField(
        label=_("Integer (text input)"),
        widget=forms.TextInput(
            attrs={
                "inputmode": "numeric",
                "pattern": r"[1-9]+",
            }
        ),
        required=False,
    )
    email = forms.EmailField(label=_("Email"), required=False)
    yes_no = forms.ChoiceField(label=_("Yes/No"), choices=BoolChoices.choices, required=False)
    yes_no_2 = forms.ChoiceField(
        label=_("Yes/No 2"), choices=BoolChoices.choices, widget=forms.RadioSelect(), required=False
    )
    boolean = forms.BooleanField(label=("Is approved"), required=False)
    date = forms.DateField(label=_("Date"), required=False)
    time = forms.TimeField(label=_("Time"), required=False)
    date_time = forms.DateTimeField(label=_("Date/Time"), required=False)
    url = forms.URLField(label=_("URL"), assume_scheme="https", required=False)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(), required=False)
