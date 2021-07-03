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
        print(dir(self))
        return f"Agency({self.id}) {self.name}"

    def delete(self):
        """
        Deleting an Agency shouldn't be possible
        """
        pass


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
    description = models.TextField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, db_index=True)
    title = models.CharField(max_length=256)
    tracking_number = models.CharField(max_length=256, db_index=True, null=True)
    filed_at = models.DateField(null=True)
    estimated_response_date = models.DateField(null=True)
    last_communication_date = models.DateField(null=True)

    def __str__(self):
        return f"RecordRequest({self.id}) {self.title} to {self.agency} with status {self.status}"

    def delete(self):
        """
        Deleteing a request shouldn't be possible. Instead change the status.
        """
        pass

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
    title = models.CharField(max_length=256)
    description = models.TextField(null=True)

    def __str__(self):
        return f"RecordRequestFile({self.id}) {self.title} for {self.request}"
