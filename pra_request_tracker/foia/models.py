from django.db import models

from pra_request_tracker.users.models import User


class FoiaRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    agency = models.CharField(max_length=100)

    def __str__(self):
        return f"FoiaRequest({self.id}) to {self.agency}"


class FoiaRequestFile(models.Model):
    request = models.ForeignKey(
        FoiaRequest,
        on_delete=models.CASCADE,
    )
    url = models.URLField()
    description = models.TextField(null=True)

    def __str__(self):
        return f"FoiaRequestFile({self.id}) for {self.request}"
