# -*- coding: utf-8 -*-
import copy
from intake.models import EventPerson


def create_person_model(data=None, email_address=None, zip_code=None):
    """Create an event person given an email, zip, and the data from AN."""
    try:
        if not data or zip_code != data['postal_addresses'][0]['postal_code']:
            person = EventPerson(email_address=email_address, zip_code=zip_code)
            person.save()
            return person
    except Exception as e:
        print(e)
        person = EventPerson(email_address=email_address, zip_code=zip_code)
        person.save()
        return person

    person = EventPerson(email_address=email_address)

    try:
        address_data = data.get('postal_addresses', []).pop(0)
        person.street_address_one = address_data.get('address_lines').pop(0)
        if address_data.get('address_lines'):
            person.street_address_two = address_data.get('address_lines').pop(0)
        person.city = address_data.get('locality', '')
        person.state = address_data.get('region', '')
    except IndexError:
        person.street_address_one = ''
        person.street_address_two = ''
        person.city = ''
        person.state = ''

    person.first_name = data.get('given_name', '')
    person.last_name = data.get('family_name', '')

    try:
        person.action_network_id = data.get('identifiers', None).pop(0).replace('action_network:', '')
    except IndexError:
        person.action_network_id = None

    person.zip_code = zip_code
    person.phone_number = data.get('custom_fields', {}).get('Phone Number')

    person.save()

    return person


def osdi_to_person(data):
    """Convert the JSON from AN to filter down to a person obj."""
    try:
        people = copy.deepcopy(data['_embedded']['osdi:people'])
    except KeyError:
        return None

    # If there are no people in the list, then the person should
    # be redirected to sign up, since they're not in the system.
    if len(people) == 0:
        return None

    return people[0]
