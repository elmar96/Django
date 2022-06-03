from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import EmailField

from .models import CustomUser


class RegistrationForm(UserCreationForm):
    GENDER_TYPE = (
        ("Male", "Male"),
        ("FeMale", "FeMale"),
        ("Other", "Other")
    )
    OCCUPATIONS = (
        ("Student", "Student"),
        ("Worker", "Worker"),
        ("Jobless", "Jobless"),
        ("Retired", "Retired")
    )
    LIST_OF_CONTINENTS = (
        ("Asia", "Asia"),
        ("Africa", "Africa"),
        ("Europe", "Europe"),
        ("North America", "North America"),
        ("South America", "South America"),
        ("Australia/Oceania", "Australia/Oceania"),
        ("Antarctica", "Antarctica"),
    )
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    phone_number = forms.CharField(required=True)
    code_word = forms.CharField(required=True)
    occupation = forms.ChoiceField(choices=OCCUPATIONS, required=True)
    continents = forms.ChoiceField(choices=LIST_OF_CONTINENTS, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "gender",
            "occupation",
            "continents",
            "code_word"
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __int__(self, *args, **kwargs):
        super(LoginForm, self).__int__(*args, **kwargs)

    email = EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "please type email",
                "id": "email"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "please type password",
                "id": "password"
            }
        )

    )