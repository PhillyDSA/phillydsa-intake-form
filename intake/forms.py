# -*- coding: utf-8 -*-
from django import forms
from localflavor.us.forms import USZipCodeField

from intake.models import EventPerson


class IntakeForm(forms.Form):
    """First form to get email & zip code."""

    email_address = forms.EmailField(label="Email")
    zip_code = USZipCodeField()


class NewMemberSigninForm(forms.ModelForm):
    """Gets a member's information and saves model."""

    class Meta:
        """Set model type and fields."""

        model = EventPerson
        fields = '__all__'
