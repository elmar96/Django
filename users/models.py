from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


class CustomUser(User):
    GENDER_TYPE = (("Male", "Male"), ("FeMale", "FeMale"), ("Other", "Other"))
    OCCUPATIONS = (
        ("Student", "Student"),
        ("Worker", "Worker"),
        ("Jobless", "Jobless"),
        ("Retired", "Retired"),
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
    gender = models.CharField(choices=GENDER_TYPE, max_length=100)
    phone_number = models.CharField(max_length=255)
    code_word = models.CharField(max_length=200)
    occupations = models.CharField(choices=OCCUPATIONS, max_length=100)
    continents = models.CharField(choices=LIST_OF_CONTINENTS, max_length=100)
