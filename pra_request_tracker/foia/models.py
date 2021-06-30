from django.db import models

from pra_request_tracker.users.models import User


class FoiaRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    agency = models.TextField()


class FoiaRequestFile(models.Model):
    request = models.ForeignKey(
        FoiaRequest,
        on_delete=models.CASCADE,
    )
    url = models.URLField()
    description = models.TextField(null=True)
