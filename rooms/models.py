from django.db import models
from django.forms import IntegerField
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item for many2many relationship."""

    name = models.CharField(max_length=80, default="")
    subtitle = models.CharField(max_length=100, default="")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class RoomType(AbstractItem):
    """RoomType Model Definition."""

    class Meta:
        verbose_name = "Room Type"
        ordering = ("name",)


class Amenity(AbstractItem):
    """Amenity Model Definition."""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model Definition."""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule Model Definition."""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition."""

    caption = models.CharField(max_length=100)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
