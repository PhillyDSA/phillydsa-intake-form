# -*- coding: utf-8 -*-

"""Views for intake form"""

import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView

from intake import forms as intake_forms
from intake.models import EventPerson
from intake.utils import create_person_model, osdi_to_person

from pyactionnetwork import ActionNetworkApi

API = ActionNetworkApi(api_key="test")

logger = logging.getLogger(__name__)


def index(request):
    """Get user email + zip and validate against AN."""
    args = {}
    args['form'] = intake_forms.IntakeForm()

    if request.method == 'POST':
        form = intake_forms.IntakeForm(request.POST)
        if form.is_valid():
            email_address, zip_code = (form.cleaned_data.get('email_address'),
                                       form.cleaned_data.get('zip_code'))

            data = API.get_person(search_string=email_address)
            person = osdi_to_person(data)

            event_person = create_person_model(data=person,
                                               email_address=email_address,
                                               zip_code=zip_code)
            return HttpResponseRedirect(reverse('intake:confirm',
                                                kwargs={'pk': event_person.id}))

        else:
            args['form'] = intake_forms.IntakeForm(request.POST)
            return render(request, 'intake/index.html', args)
    else:
        return render(request, 'intake/index.html', args)


class NewMemberUpdate(UpdateView):
    """Update a member's information and save to model"""

    model = EventPerson
    fields = [
        'email_address',
        'first_name',
        'last_name',
        'street_address_one',
        'street_address_two',
        'city',
        'state',
        'zip_code',
        'phone_number',
    ]
    template_name = 'intake/confirm.html'
    success_url = '/'

    def post(self, *args, **kwargs):
        """Post to local system and also create or update person in AN"""
        resp = super(NewMemberUpdate, self).post(*args, **kwargs)
        person_id = self.request.resolver_match.kwargs['pk']
        person = EventPerson.objects.get(id=person_id)
        person.save()

        an_data = API.create_person(
            email=person.email_address,
            given_name=person.first_name,
            family_name=person.last_name,
            address=[person.street_address_one, person.street_address_two],
            city=person.city,
            state=person.state,
            country='US',
            postal_code=person.zip_code,
            custom_fields={'Phone Number': person.phone_number},
            tags=['2017_04_general_meeting']
        )
        print(an_data)
        return resp
