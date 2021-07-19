from django.db import models
from django.utils.functional import cached_property

from pra_request_tracker.users.models import User


class BaseModel(models.Model):
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(editable=False, auto_now=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)


class Agency(BaseModel):
    class Meta:
        verbose_name_plural = "Agencies"

    name = models.CharField(max_length=256, unique=True, db_index=True)

    def __str__(self):
        return f"Agency({self.id}) {self.name}"

    def delete(self):
        """Prevent deleting an Agency."""
        raise NotImplementedError("Deleting Agencies not allowed")

    @cached_property
    def request_count(self):
        return self.recordrequest_set.count()


class RecordRequest(BaseModel):
    class Status(models.TextChoices):
        SUBMITTED = "submitted", "Processing"
        AWAITING_ACKNOWLEDGEMENT = "ack", "Awaiting Acknowledgement"
        PROCESSED = "processed", "Awaiting Response"
        APPEALING = "appealing", "Awaiting Apeal"
        FIX = "fix", "Fix Required"
        PAYMENT = "payment", "Payment Required"
        LAWSUIT = "lawsuit", "In Litigation"
        REJECTED = "rejected", "Rejected"
        NO_DOCS = "no_docs", "No Responsive Documents"
        DONE = "done", "Completed"
        PARTIAL = "partial", "Partially Completed"
        ABANDONED = "abandoned", "Withdrawn"
        IN_REVIEW = "review", "In Review"
        INSTALLMENTS = "install", "Installments"

    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, db_index=True)
    title = models.CharField(max_length=256)
    tracking_number = models.CharField(max_length=256, db_index=True, null=True)
    filed_at = models.DateField(null=True, blank=True)
    estimated_response_date = models.DateField(null=True, blank=True)
    last_communication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"RecordRequest({self.id}) {self.title} to {self.agency} with status {self.status}"

    def delete(self):
        """Prevent deleting a request.

        Instead change the status.
        """
        raise NotImplementedError("Deleting RecordRequests not allowed")

    @property
    def status_label(self):
        return self.Status(self.status).label

    @cached_property
    def files(self):
        return self.recordrequestfile_set.all()


class RecordRequestFile(BaseModel):
    request = models.ForeignKey(
        RecordRequest,
        on_delete=models.CASCADE,
    )
    file = models.FileField()
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"RecordRequestFile({self.id}) {self.title} for {self.request}"

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.file.name
        super().save(*args, **kwargs)
