# -*- coding: utf-8 -*-

"""Models for intake form"""

from django.db import models
from localflavor.us.models import (
    USPostalCodeField,
    PhoneNumberField,
    USZipCodeField,
)


class EventPerson(models.Model):
    """Model for a person attending an event"""

    email_address = models.EmailField()
    street_address_one = models.CharField(max_length=255)
    street_address_two = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USPostalCodeField(default="PA")
    zip_code = USZipCodeField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.email_address
