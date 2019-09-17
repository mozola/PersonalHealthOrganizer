from django import forms

from .models import Meal
from .models import Component
from .models import Product


class NewComponent(forms.ModelForm):

    class Meta:
        model = Component
        fields = ('name', 'waste', 'units', 'calories')


class NewProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('component', 'count', 'units', 'calories')
        widgets = {'calories': forms.TextInput(attrs={'disabled': True})}

    def clean_calories(self, *args, **kwargs):
        """
            When user submit this form than mechanism
            sum all callories Components
        """
        components = self.clean_data.get('component')
        callories = [i.calories for i in components]
        return sum(callories)


class NewMealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ('name', 'description', 'products', 'callories', 'types', 'state')
        widgets = {'callories': forms.TextInput(attrs={'disabled': True}),
                   'products': forms.CheckboxSelectMultiple()}

    def clean_callories(self, *args, **kwargs):
        """
            When user submit this form than mechanism
            sum all callories products
        """
        products = self.cleaned_data.get('products')
        calories = [i.calories for i in products]
        return sum(calories)
