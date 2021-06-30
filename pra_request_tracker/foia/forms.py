from django import forms

from pra_request_tracker.foia.models import FoiaRequest, FoiaRequestFile


class FoiaRequestForm(forms.ModelForm):
    class Meta:
        model = FoiaRequest

        fields = ("requester", "description", "agency")


class FoiaRequestFileForm(forms.ModelForm):
    class Meta:
        model = FoiaRequestFile

        fields = ("request", "url", "description")
