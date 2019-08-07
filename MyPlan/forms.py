from django import forms
from .models import Sprints

class StartNewSprintForm(forms.Form):
    component = forms.ModelChoiceField(queryset=Sprints.objects.all())
    status = forms.BooleanField()

class UpdateNewSprintForm(forms.Form):
    pass
