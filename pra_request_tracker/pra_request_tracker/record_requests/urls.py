from django.urls import path

from .views import AgencyDetailView, AgencyListView, RecordRequestDetailView


app_name = "record_requests"
urlpatterns = [
    path("agencies/", view=AgencyListView.as_view(), name="agencies"),
    path("agency/<str:name>/", view=AgencyDetailView.as_view(), name="agency-detail"),
    path("<int:pk>/", view=RecordRequestDetailView.as_view(), name="request-detail"),
]
