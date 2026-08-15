from django.contrib.auth.forms import UserCreationForm

from agency.models import Redactor


class RedactorCreationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ("username", "first_name", "last_name", "years_of_experience")