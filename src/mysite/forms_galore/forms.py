from django import forms
from django.db.models import TextChoices
from django.utils.translation import pgettext_lazy


class SampleForm(forms.Form):
    """Form containing a collection of different fields."""

    class BoolChoices(TextChoices):
        YES = "y", pgettext_lazy("Boolean choice", "Yes")
        NO = "n", pgettext_lazy("Boolean choice", "No")

    required = forms.CharField(
        label=pgettext_lazy("Field label", "Required"),
        help_text=pgettext_lazy("Field help text", "Leave this field empty to trigger an error."),
    )
    disabled = forms.CharField(
        label=pgettext_lazy("Field label", "Disabled"),
        disabled=True,
        required=False,
    )
    integer = forms.IntegerField(
        label=pgettext_lazy("Field label", "Integer (number input)"),
        required=False,
    )
    # Numeric text input instead of a number input:
    # https://technology.blog.gov.uk/2020/02/24/why-the-gov-uk-design-system-team-changed-the-input-type-for-numbers/
    integer_as_text = forms.IntegerField(
        label=pgettext_lazy("Field label", "Integer (text input)"),
        widget=forms.TextInput(
            attrs={
                "inputmode": "numeric",
                "pattern": r"[1-9]+",
            }
        ),
        required=False,
    )
    email = forms.EmailField(
        label=pgettext_lazy("Field label", "Email"),
        required=False,
    )
    yes_no = forms.ChoiceField(
        label=pgettext_lazy("Field label", "Yes/No"),
        choices=BoolChoices.choices,
        required=False,
    )
    yes_no_2 = forms.ChoiceField(
        label=pgettext_lazy("Field label", "Yes/No 2"),
        choices=BoolChoices.choices,
        widget=forms.RadioSelect(),
        required=False,
    )
    boolean = forms.BooleanField(
        label=("Is approved"),
        required=False,
    )
    date = forms.DateField(
        label=pgettext_lazy("Field label", "Date"),
        required=False,
    )
    time = forms.TimeField(
        label=pgettext_lazy("Field label", "Time"),
        required=False,
    )
    date_time = forms.DateTimeField(
        label=pgettext_lazy("Field label", "Date/Time"),
        required=False,
    )
    url = forms.URLField(
        label=pgettext_lazy("Field label", "URL"),
        assume_scheme="https",
        required=False,
    )
    password = forms.CharField(
        label=pgettext_lazy("Field label", "Password"),
        widget=forms.PasswordInput(),
        required=False,
    )
