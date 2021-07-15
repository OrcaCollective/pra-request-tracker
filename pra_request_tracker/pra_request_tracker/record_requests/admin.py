from django.contrib import admin

from .forms import AgencyForm, RecordRequestFileForm, RecordRequestForm
from .models import Agency, RecordRequest, RecordRequestFile


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    form = AgencyForm
    list_display = ("name",)


@admin.register(RecordRequest)
class RecordRequestAdmin(admin.ModelAdmin):
    form = RecordRequestForm
    list_display = (
        "title",
        "agency",
        "tracking_number",
        "status",
        "filed_at",
        "estimated_response_date",
        "last_communication_date",
        "updated_at",
    )


@admin.register(RecordRequestFile)
class RecordRequestFileAdmin(admin.ModelAdmin):
    form = RecordRequestFileForm
    list_display = ("title", "request")
