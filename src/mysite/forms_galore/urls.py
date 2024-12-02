from django.urls import path

from mysite.forms_galore.views import SampleFormView


app_name = "forms_galore"
urlpatterns = [
    path("sample-form/", SampleFormView.as_view(), name="sample_form"),
]
