# -*- coding: utf-8 -*-
from intake.models import EventPerson


def create_person_model(data, email_address, zip_code):
    """Create an event person given an email, zip, and the data from AN."""
    person, _ = EventPerson.objects.get_or_create(email_address=email_address)
    address_data = data.get('postal_addresses', [None])[0]

    person.first_name = data.get('given_name', None)
    person.last_name = data.get('family_name', None)
    action_network_id = data.get('identifiers', [None])[0]

    if action_network_id:
        person.action_network_id = action_network_id.replace('action_network:', '')

    person.zip_code = zip_code
    if address_data:
        person.street_address_one = address_data.get('address_lines', [None])[0]
        if len(address_data.get('address_lines', [None])) > 1:
            person.street_address_two = address_data.get('address_lines')[1]
        else:
            person.street_address_two = None
        person.city = address_data.get('locality', None)
        person.state = address_data.get('region', None)
    person.phone_number = data.get('custom_fields', {}).get('Phone Number')

    person.save()

    return person


def osdi_to_person(data):
    """Convert the JSON from AN to filter down to a person obj."""
    people = data['_embedded']['osdi:people']

    # If there are no people in the list, then the person should
    # be redirected to sign up, since they're not in the system.
    if len(people) == 0:
        return None

    return people[0]
