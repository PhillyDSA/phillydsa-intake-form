# -*- coding: utf-8 -*-

"""Tests for intake form"""
import json

from django.urls import reverse
from django.test import (
    TestCase,
    Client,
)

from intake.forms import IntakeForm
from intake.models import EventPerson
from intake.utils import create_person_model, osdi_to_person

with open('intake/test_data/people.json', 'r') as f:
    SAMPLE_PERSON_DATA1 = json.loads(f.read())

with open('intake/test_data/people_two_line_address.json', 'r') as f:
    SAMPLE_PERSON_DATA2 = json.loads(f.read())

with open('intake/test_data/people_no_address.json', 'r') as f:
    SAMPLE_PERSON_DATA3 = json.loads(f.read())

with open('intake/test_data/people_no_action_network_id.json', 'r') as f:
    SAMPLE_PERSON_DATA4 = json.loads(f.read())


class ModelTests(TestCase):
    def test_create_person_with_data(self):
        data = osdi_to_person(SAMPLE_PERSON_DATA1)
        person = create_person_model(data=data,
                                     email_address='testuser@example.com',
                                     zip_code='19143')
        assert person.email_address == 'testuser@example.com'
        assert person.first_name == 'Test'
        assert person.last_name == 'User'
        assert person.phone_number == '555-001-0022', person.phone_number
        assert person.action_network_id == 'asdfasdf-asdfasdf-asdfasdf'
        assert person.street_address_one == '10001 Test Ave'
        assert not person.street_address_two
        assert person.city == 'Philadelphia'
        assert person.state == 'PA'
        assert str(person) == 'testuser@example.com'

    def test_create_person_with_two_line_address(self):
        data = osdi_to_person(SAMPLE_PERSON_DATA2)
        person = create_person_model(data=data,
                                     email_address='testuser@example.com',
                                     zip_code='19143')
        assert person.street_address_two == 'Apt 2'

    def test_create_person_with_no_address(self):
        data = osdi_to_person(SAMPLE_PERSON_DATA3)
        person = create_person_model(data=data,
                                     email_address='testuser@example.com',
                                     zip_code='19143')
        assert not person.street_address_two

    def test_create_person_with_no_action_network_id(self):
        data = osdi_to_person(SAMPLE_PERSON_DATA4)
        person = create_person_model(data=data,
                                     email_address='testuser@example.com',
                                     zip_code='19143')
        assert not person.street_address_two

    def test_create_person_without_data(self):
        person = create_person_model(email_address='testuser@example.com',
                                     zip_code='19143')
        assert person.email_address == 'testuser@example.com'
        assert person.zip_code == '19143'
        assert person.id is not None

    def test_osdi_errors(self):
        data = {'in': 'correct'}
        person = osdi_to_person(data)
        assert person is None

        data = {'_embedded': {'osdi:people': []}}
        person = osdi_to_person(data)
        assert person is None


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.person = create_person_model(email_address='testuser@example.com',
                                          zip_code='19143')

    def test_event_person_reverse_url(self):
        assert self.person.get_absolute_url() == '/detail/1/', self.person.get_absolute_url()
        assert reverse('intake:detail', kwargs={'pk': self.person.id}) == '/detail/1/'

    def test_event_person_detail_view(self):
        resp = self.client.get(reverse('intake:detail', kwargs={'pk': self.person.id}))
        assert resp.status_code == 200
        assert isinstance(resp.context_data['object'], EventPerson)
        assert resp.context_data['object'].zip_code == '19143'

    def test_get_index(self):
        resp = self.client.get(reverse('intake:index'))
        assert resp.status_code == 200
        self.assertTemplateUsed(resp, 'intake/index.html')
        assert isinstance(resp.context['form'], IntakeForm)

    def test_post_index(self):
        resp = self.client.post(reverse('intake:index'),
                                {'email_address': 'testuser@example.com', 'zip_code': '19134'})
        assert resp.status_code == 302

        resp = self.client.post(reverse('intake:index'),
                                {'email_address': 'testuser@example.com', 'zip_code': ''})
        assert resp.status_code == 200
        assert 'This field is required.' in resp.content.decode('utf8')
        assert resp.context['form'].errors['zip_code'][0] == 'This field is required.'
