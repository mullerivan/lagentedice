# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from django import forms

from django_localflavor_nz.forms import NZPhoneNumberField
from django.utils.translation import ugettext_lazy as _
from escrow.accounts.models import User

from nocaptcha_recaptcha.fields import NoReCaptchaField
from django_password_strength.widgets import PasswordStrengthInput, \
    PasswordConfirmationInput

from allauth.account.forms import SignupForm
from allauth.utils import set_form_field_order
from django.forms.widgets import Select

__all__ = (
    'SignupForm',    
)





class SignupForm(SignupForm):
    """Base registration form for both individual and company forms."""

    account_type = forms.ChoiceField(
        label=_("You are going to SignUp  as a:"),
        choices=AccountType.CHOICES,
        widget=forms.RadioSelect)

    first_name = forms.CharField(
        label=_("Your first name"),
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'John',
            'maxlength': 30,
        }))

    email = forms.EmailField(
        label='Email',
        max_length=250,
        widget=forms.EmailInput())

    password1 = forms.CharField(
        label='Password',
        widget=PasswordStrengthInput(),
        min_length=5)

    password2 = forms.CharField(
        label='Confirm Password',
        widget=PasswordConfirmationInput(),
        min_length=5)

    captcha = NoReCaptchaField(
        label='')

    def clean(self):
        """Check passwords are equal."""
        # skip SignUp clean because the error message is not going to the field
        super(SignupForm, self).clean()
        if 'password1' in self.cleaned_data.keys() and \
                        'password2' in self.cleaned_data.keys() and \
                        self.cleaned_data['password1'] != self.cleaned_data[
                    'password2']:
            self.add_error('password1',
                           'You must type the same password each time.')

        return self.cleaned_data

    def clean_email(self):
        """Check email address is unique."""
        qs = User.objects.filter(email=self.cleaned_data['email'])
        if qs.count() > 0:
            raise forms.ValidationError(
                'A user with that email address has already subscribed.')
        return self.cleaned_data['email']

    def save(self, request):
        user = super(EscrowSignupForm, self).save(request)
        request.session['account_type'] = self.cleaned_data['account_type']
        return user

    def __init__(self, *args, **kwargs):
        super(EscrowSignupForm, self).__init__(*args, **kwargs)
        set_form_field_order(self, ['account_type', 'email', 'first_name',
                                    'password1', 'password2', 'captcha'])


