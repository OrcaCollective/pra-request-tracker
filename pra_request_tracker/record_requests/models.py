from django.db import models

from pra_request_tracker.users.models import User


class Agency(models.Model):
    class Meta:
        verbose_name_plural = "Agencies"

    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"Agency({self.id}) {self.name}"

    def delete(self):
        """
        Deleting an Agency shouldn't be possible
        """
        pass


class RecordRequest(models.Model):
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

    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, db_index=True)

    def __str__(self):
        return f"RecordRequest({self.id}) to {self.agency}"

    def delete(self):
        """
        Deleteing a request shouldn't be possible. Instead change the status.
        """
        pass


class RecordRequestFile(models.Model):
    request = models.ForeignKey(
        RecordRequest,
        on_delete=models.CASCADE,
    )
    file = models.FileField()
    description = models.TextField(null=True)

    def __str__(self):
        return f"RecordRequestFile({self.id}) for {self.request}"
