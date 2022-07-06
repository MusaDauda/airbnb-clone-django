from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    """Time Stamped Model Definition."""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
