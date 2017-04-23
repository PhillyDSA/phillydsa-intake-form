# -*- coding: utf-8 -*-

"""Models for intake form"""

from django.db import models
from django.urls import reverse
from localflavor.us.models import (
    USPostalCodeField,
    PhoneNumberField,
    USZipCodeField,
)


class EventPerson(models.Model):
    """Model for a person attending an event"""

    email_address = models.EmailField()
    first_name = models.CharField(max_length=255, blank=True, null=True, default='')
    last_name = models.CharField(max_length=255, blank=True, null=True, default='')
    action_network_id = models.CharField(max_length=255, blank=True, null=True, default='')
    street_address_one = models.CharField(max_length=255, blank=True, null=True, default='')
    street_address_two = models.CharField(max_length=255, blank=True, null=True, default='')
    city = models.CharField(max_length=255, blank=True, null=True, default='')
    state = USPostalCodeField(default="PA", blank=True, null=True)
    zip_code = USZipCodeField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, default='')

    def __str__(self):
        return self.email_address

    def get_absolute_url(self):
        """Return default view for an EventPerson"""
        return reverse('intake:detail', kwargs={'pk': self.pk})
