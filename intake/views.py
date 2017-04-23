# -*- coding: utf-8 -*-

"""Views for intake form"""

import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

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


class EventPersonDetailView(DetailView):
    """Show a member's information"""

    model = EventPerson
    template_name = 'intake/detail.html'
