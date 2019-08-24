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
        fields = ('name', 'description', 'products',
                  'callories', 'types', 'state')
