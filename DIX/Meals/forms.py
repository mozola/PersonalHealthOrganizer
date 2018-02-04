#coding=utf-8
from django import forms


class NewMealsForm(forms.ModelForm):

    name = forms.CharField(max_length=15, label='Name')
    description = forms.CharField(max_length=15, label='Desciption')
#    components = forms.ModelMultipleChoiceField(
#                label='Choix',
#                queryset=poll.options.all().order_by('?'),
#                widget=CheckboxSelectMultiple()
#    )
    callories = forms.CharField(max_length=15, label='Name')
#    type = forms.ModelMultipleChoiceField(
#                    widget=forms.CheckboxSelectMultiple,
#                    required=True)

    image =forms.ImageField()