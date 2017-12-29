# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Meals


def index(request):
    return render(request, 'Meals/index.html', {'all_meals': Meals.objects.all()})


def details(request, meal_id):
    return render(request, 'Meals/details.html', {'meals_id': Meals.objects.get(pk = meal_id)})