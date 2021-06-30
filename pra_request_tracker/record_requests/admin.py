from django.contrib import admin  # noqa

from pra_request_tracker.record_requests.models import RecordRequest
from pra_request_tracker.record_requests.models import RecordRequestFile
from pra_request_tracker.record_requests.forms import RecordRequestForm
from pra_request_tracker.record_requests.forms import RecordRequestFileForm


@admin.register(RecordRequest)
class RecordRequestAdmin(admin.ModelAdmin):
    form = RecordRequestForm


@admin.register(RecordRequestFile)
class RecordRequestFileAdmin(admin.ModelAdmin):
    form = RecordRequestFileForm
