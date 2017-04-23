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
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    action_network_id = models.CharField(max_length=255, blank=True, null=True)
    street_address_one = models.CharField(max_length=255, blank=True, null=True)
    street_address_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = USPostalCodeField(default="PA", blank=True, null=True)
    zip_code = USZipCodeField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.email_address
