from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from .models import Agency, RecordRequest


class AgencyDetailView(LoginRequiredMixin, DetailView):
    model = Agency
    slug_field = "name"
    slug_url_kwarg = "name"


class RecordRequestDetailView(LoginRequiredMixin, DetailView):
    model = RecordRequest
