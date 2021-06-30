from django.contrib import admin  # noqa

from pra_request_tracker.foia.models import FoiaRequest
from pra_request_tracker.foia.models import FoiaRequestFile
from pra_request_tracker.foia.forms import FoiaRequestForm
from pra_request_tracker.foia.forms import FoiaRequestFileForm


@admin.register(FoiaRequest)
class FoiaRequestAdmin(admin.ModelAdmin):
    form = FoiaRequestForm


@admin.register(FoiaRequestFile)
class FoiaRequestFileAdmin(admin.ModelAdmin):
    form = FoiaRequestFileForm
