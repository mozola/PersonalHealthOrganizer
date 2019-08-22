from django import forms

from .models import Meal
from .models import Component
from .models import Product

class NewComponent(forms.ModelForm):

    class Meta:
        model = Component
        fields = ('name', 'waste', 'units')


class NewProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('component', 'count', 'units')


class NewMealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ('name', 'description', 'products', 'callories', 'types', 'state')
    """
    choices = (
        ('sniadanie', 'sniadanie'),
        ('podwieczorek', 'podwieczorek'),
        ('obiad', 'obiad'),
        ('kolacja', 'kolacja')
    )

    units = (
        ('sztuk', 'sztuk'),
        ('gramy', 'gramy'),
        ('litry', 'litry')
    )
    name = forms.CharField(label='Meal name', max_length=30)
    description = forms.CharField(widget = forms.TextInput())
    component = forms.ModelChoiceField(queryset=Component.objects.all())
    product_count = forms.IntegerField()
    product_units = forms.CharField(max_length=10, widget=forms.Select(choices= units))
    callories = forms.IntegerField()
    types = forms.CharField(max_length=10, widget=forms.Select(choices= choices))
    """