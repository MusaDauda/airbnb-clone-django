from email.policy import default
from django.db import models
from django.forms import IntegerField
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item for many2many relationship."""

    name = models.CharField(max_length=80, default="")
    subtitle = models.CharField(max_length=100, default="")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class RoomType(AbstractItem):
    pass


class Room(core_models.TimeStampedModel):
    """The Room  Model Definition."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    address = models.CharField(max_length=255)
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name
