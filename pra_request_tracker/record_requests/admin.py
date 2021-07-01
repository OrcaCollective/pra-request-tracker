from django.contrib import admin  # noqa

from .models import Agency
from .models import RecordRequest
from .models import RecordRequestFile
from .forms import AgencyForm
from .forms import RecordRequestForm
from .forms import RecordRequestFileForm


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    form = AgencyForm


@admin.register(RecordRequest)
class RecordRequestAdmin(admin.ModelAdmin):
    form = RecordRequestForm


@admin.register(RecordRequestFile)
class RecordRequestFileAdmin(admin.ModelAdmin):
    form = RecordRequestFileForm
