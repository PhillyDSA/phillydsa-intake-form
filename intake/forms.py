from django import forms
from localflavor.us.forms import USZipCodeField


class IntakeForm(forms.Form):
    """First form to get email & zip code."""
    email_address = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={
            'placeholder': 'email',
            'required': 'true',
            'autocomplete': 'off'
        }))
    zip_code = USZipCodeField()


class ContactInformationConfirmationForm(forms.Form):
    """Confirm a member's address, tel information"""
    pass
