from django import forms

from pra_request_tracker.record_requests.models import RecordRequest
from pra_request_tracker.record_requests.models import RecordRequestFile


class RecordRequestForm(forms.ModelForm):
    class Meta:
        model = RecordRequest

        fields = ("requester", "description", "agency")


class RecordRequestFileForm(forms.ModelForm):
    class Meta:
        model = RecordRequestFile

        fields = ("request", "url", "description")
