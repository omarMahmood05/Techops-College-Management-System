from dataclasses import fields
from django import forms
from techops.models import *

class edited_form(forms.ModelForm):
    class Meta:
        model = faculty
        fields = "__all__"