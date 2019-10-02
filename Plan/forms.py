from django import forms
from .models import Sprint, SinglePlan


class StartNewPlanForm(forms.Form):
    component = forms.ModelChoiceField(queryset=Sprint.objects.all())
    status = forms.BooleanField()


class StartNewDayPlanForm(forms.ModelForm):
    class Meta:
        model = SinglePlan
        fields = ('plan_date', 'meals')
        widgets = {'meals': forms.CheckboxSelectMultiple()}


class PlanCreateForm(forms.ModelForm):

    class Meta:
        model = Sprint
        fields = ('sprint_name', 'sprint_parameters', 'sprint_status')
        widgets = {'sprint_parameters':  forms.CheckboxSelectMultiple()}
