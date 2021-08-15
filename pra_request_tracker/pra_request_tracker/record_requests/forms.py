from django import forms

from .models import Agency, Correspondence, RecordRequest, RecordRequestFile


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ("name",)


class RecordRequestForm(forms.ModelForm):
    class Meta:
        model = RecordRequest
        fields = (
            "requester",
            "agency",
            "title",
            "description",
            "status",
            "tracking_number",
            "filed_at",
            "estimated_response_date",
            "last_communication_date",
        )


class RecordRequestFileForm(forms.ModelForm):
    class Meta:
        model = RecordRequestFile
        fields = ("request", "title", "description", "file", "correspondence")


class CorrespondenceForm(forms.ModelForm):
    class Meta:
        model = Correspondence
        fields = ("request", "contact_address", "date", "subject", "body")
