# -*- coding: utf-8 -*-

"""Tests for intake form"""
import json

from django.test import TestCase

# Create your tests here.
from intake.utils import create_person_model, osdi_to_person

with open('intake/test_data/people.json', 'r') as f:
    SAMPLE_PERSON_DATA = json.loads(f.read())


class ModelTests(TestCase):
    def test_create_person(self):
        data = osdi_to_person(SAMPLE_PERSON_DATA)
        person = create_person_model(data=data,
                                     email_address='testuser@example.com',
                                     zip_code='19143')
        assert person.email_address == 'testuser@example.com'
        assert person.first_name == 'Test'
        assert person.last_name == 'User'
        assert person.phone_number == '555-001-0022', person.phone_number
        assert person.action_network_id == 'asdfasdf-asdfasdf-asdfasdf'
        assert person.street_address_one == '10001 Test Ave'
        assert person.street_address_two is None
        assert person.city == 'Philadelphia'
        assert person.state == 'PA'
