from django import forms
from django.contrib.auth.forms import (PasswordResetForm, UserChangeForm,
                                       UserCreationForm)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from .models import Resident

# Form to create a new Resident instance


class ResidentCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    flatNo = forms.CharField(widget=forms.TextInput(attrs={}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={}))
    # for confirming the password
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={}))

    class Meta:
        model = Resident
        fields = {"username", "flatNo", 'email',
                  "password1", "password2", "is_verified"}
    # For Checking if the email entered already exists

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = Resident.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError(
                "Cannot use this email. It's already registered")
        return email

# Form to update a Resident instance


class ResidentUpdateForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    is_verified = forms.BooleanField()
    email = forms.EmailField()
    visible = forms.BooleanField()

    class Meta:
        model = Resident
        fields = "__all__"

# Form to enter the email for sending the password reset link


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        # To check if the email exists
        if not Resident.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError(
                "There is no user registered with the specified email address!")

        return email
