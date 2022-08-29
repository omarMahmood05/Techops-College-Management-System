from dataclasses import fields
from django import forms
from techops.models import *

class edited_form(forms.ModelForm):
    class Meta:
        models =faculty
        fields="__all__"