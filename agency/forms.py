from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from agency.models import NewsPaper, Redactor, Topic


class RedactorCreationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ("username", "first_name", "last_name", "years_of_experience")


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        fields = "__all__"
        model = NewsPaper
