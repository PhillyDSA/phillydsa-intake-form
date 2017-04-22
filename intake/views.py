# -*- coding: utf-8 -*-

"""Views for intake form"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from intake.forms import IntakeForm

from pyactionnetwork import ActionNetworkApi

API = ActionNetworkApi(api_key="test")


def osdi_to_person(data):
    """Convert the JSON from AN to filter down to a person obj."""

    try:
        people = data['_embedded']['osdi:people']

        # If there are no people in the list, then the person should
        # be redirected to sign up, since they're not in the system.
        if len(people) == 0:
            return None
    except KeyError:
        raise  # raise a 500 error cause AN is broken.

    return people[0]


def index(request):
    """Get user email + zip and validate against AN."""
    args = {}
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            email_address, zip_code = (form.cleaned_data.get('email_address'),
                                       form.cleaned_data.get('zip_code'))

            an_data = API.get_person(search_string=email_address)
            person = osdi_to_person(an_data)

            if not person:
                return HttpResponseRedirect(reverse('intake:new_member'))

            try:
                an_zip_code = person['postal_addresses'][0]['postal_code']
            except KeyError:
                # if we don't have their physical address in the system, send
                # them to the sign up page.
                return HttpResponseRedirect('TODO')

            # if their zip code checks out, redirect them to confirm
            # their address information.
            if zip_code == an_zip_code:
                return HttpResponseRedirect('intake:confirm')
        else:
            args['form'] = IntakeForm(request.POST)
            return render(request, 'intake/index.html', args)
    else:
        return render(request, 'intake/index.html', args)


def new_member_signup(request):
    """Sign up a new member with AN"""
    pass


def confirm_member_info(request):
    """Confirm a member's information with the data in AN."""
    pass
