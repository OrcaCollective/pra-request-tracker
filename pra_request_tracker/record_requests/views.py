from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Agency, RecordRequest


class AgencyListView(LoginRequiredMixin, ListView):
    model = Agency


class AgencyDetailView(LoginRequiredMixin, DetailView):
    model = Agency
    slug_field = "name"
    slug_url_kwarg = "name"


class RecordRequestDetailView(LoginRequiredMixin, DetailView):
    model = RecordRequest
