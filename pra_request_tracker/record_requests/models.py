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
        OPENED = "opened", "opened"
        PENDING = "pending", "pending"
        SENT = "sent", "sent"
        CLOSED = "closed", "closed"

    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.OPENED
    )

    def __str__(self):
        return f"RecordRequest({self.id}) to {self.agency}"


class RecordRequestFile(models.Model):
    request = models.ForeignKey(
        RecordRequest,
        on_delete=models.CASCADE,
    )
    file = models.FileField()
    description = models.TextField(null=True)

    def __str__(self):
        return f"RecordRequestFile({self.id}) for {self.request}"
