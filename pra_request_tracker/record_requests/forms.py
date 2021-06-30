from django import forms

from pra_request_tracker.record_requests.models import Agency
from pra_request_tracker.record_requests.models import RecordRequest
from pra_request_tracker.record_requests.models import RecordRequestFile


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency

        fields = ("name",)


class RecordRequestForm(forms.ModelForm):
    class Meta:
        model = RecordRequest

        fields = ("requester", "title", "description", "agency", "status")


class RecordRequestFileForm(forms.ModelForm):
    class Meta:
        model = RecordRequestFile

        fields = ("request", "file", "description")
