from django import forms
from .models import Sprint


class StartNewSprintForm(forms.Form):
    component = forms.ModelChoiceField(queryset=Sprint.objects.all())
    status = forms.BooleanField()

class UpdateNewSprintForm(forms.Form):
    pass
