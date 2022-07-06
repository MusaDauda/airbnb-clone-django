from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model Class"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    ]

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    ]

    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(
        null=True,
        blank=True,
    )
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True)
    superhost = models.BooleanField(default=False, blank=True)
