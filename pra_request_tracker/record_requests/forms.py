from django import forms

from .models import Agency
from .models import RecordRequest
from .models import RecordRequestFile


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ("name",)


class RecordRequestForm(forms.ModelForm):
    class Meta:
        model = RecordRequest
        fields = ("requester", "agency", "title", "description", "status")


class RecordRequestFileForm(forms.ModelForm):
    class Meta:
        model = RecordRequestFile
        fields = ("request", "title", "description", "file")
