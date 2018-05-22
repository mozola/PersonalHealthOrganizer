# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings

from .models import Meal
from .models import Component

from .forms import NewMeal
from .forms import NewComponent


def single_meal(meal_type1):
    meals = []
    for meal in Meal.objects.filter(type=meal_type1):
        meals.append(meal)

    return meals


def index(request):

    return render(request, 'Meals/index.html',
                  {'breakfast': single_meal('sniadanie'),
                   'dinner': single_meal('obiad'),
                   'supper': single_meal('kolacja'),
                   'meala': settings.BASE_DIR}
                  )


def details(request, meal_id):
    return render(request, 'Meals/details.html', {'meals_id': Meal.objects.get(pk = meal_id)})


def new_meal(request):
    if request.method == "POST":
        form = NewMeal(request.POST)

        if form.is_valid():
            meal = form.save(commit=False)
            meal.save()
            return render(request, 'Meals/new_meal.html', {'state': True})

    else:
        form = NewMeal()
    return render(request, 'Meals/new_meal.html', {'form': form})

def new_component(request):
    if request.method == "POST":
        form = NewComponent(request.POST)

        if form.is_valid():
            component = form.save(commit=False)
            component.save()
            return render(request, 'Meals/new_component.html', {'state': True})

    else:
        form = NewComponent()
    return render(request, 'Meals/new_component.html', {'form': form})