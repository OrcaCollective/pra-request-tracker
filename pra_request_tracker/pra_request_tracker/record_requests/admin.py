from django.contrib import admin
from django.http import QueryDict
from django.urls import reverse
from django.utils.html import format_html

from .forms import (
    AgencyForm,
    CorrespondenceForm,
    RecordRequestFileForm,
    RecordRequestForm,
)
from .models import Agency, Correspondence, RecordRequest, RecordRequestFile


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    form = AgencyForm
    list_display = ("name", "agency_actions")
    search_fields = ("name",)

    def agency_actions(self, obj):
        query = QueryDict(mutable=True)
        query.update({"agency": obj.pk})
        return format_html(
            '<a class="button custom-action" href="{}">Add request</a>'
            '<a class="button custom-action" href="{}">View requests</a>',
            f'{reverse("admin:record_requests_recordrequest_add")}?{query.urlencode()}',
            f'{reverse("admin:record_requests_recordrequest_changelist")}?{query.urlencode()}',
        )

    agency_actions.short_description = "Actions"
    agency_actions.allow_tags = True


@admin.register(RecordRequest)
class RecordRequestAdmin(admin.ModelAdmin):
    form = RecordRequestForm
    list_display = (
        "title",
        "record_request_actions",
        "agency",
        "tracking_number",
        "status",
        "filed_at",
        "estimated_response_date",
        "last_communication_date",
        "updated_at",
    )
    search_fields = ("title", "agency", "tracking_number")
    autocomplete_fields = ("agency", "requester")

    def record_request_actions(self, obj):
        query = QueryDict(mutable=True)
        query.update({"request": obj.pk})
        return format_html(
            '<a class="button custom-action" href="{}">Add file</a>'
            '<a class="button custom-action" href="{}">View files</a>'
            '<a class="button custom-action" href="{}">Add correspondence</a>',
            f'{reverse("admin:record_requests_recordrequestfile_add")}?{query.urlencode()}',
            f'{reverse("admin:record_requests_recordrequestfile_changelist")}?{query.urlencode()}',
            f'{reverse("admin:record_requests_correspondence_add")}?{query.urlencode()}',
        )

    record_request_actions.short_description = "Actions"
    record_request_actions.allow_tags = True


@admin.register(Correspondence)
class CorrespondenceAdmin(admin.ModelAdmin):
    form = CorrespondenceForm
    list_display = ("request", "correspondence_actions", "date")
    autocomplete_fields = ("request",)
    search_fields = ("subject", "request", "to", "from")

    def correspondence_actions(self, obj):
        query = QueryDict(mutable=True)
        query.update(
            {
                "request": obj.request.pk,
                "correspondence": obj.pk,
            }
        )
        return format_html(
            '<a class="button custom-action" href="{}">Attach file</a>',
            f'{reverse("admin:record_requests_recordrequestfile_add")}?{query.urlencode()}',
        )


@admin.register(RecordRequestFile)
class RecordRequestFileAdmin(admin.ModelAdmin):
    form = RecordRequestFileForm
    list_display = ("title", "request")
    autocomplete_fields = ("request", "correspondence")
