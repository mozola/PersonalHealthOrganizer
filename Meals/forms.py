#coding=utf-8
from django import forms

from .models import Meal
from .models import Component
from .models import Product


class NewMeal(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ('name', 'description','products', 'image', 'callories', 'type')


class NewComponent(forms.ModelForm):

    class Meta:
        model = Component
        fields = ('name', 'waste', 'units')


class NewProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('component', 'count', 'units')


