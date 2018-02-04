# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from .models import Meals
from .forms import NewMealsForm


def single_meal(meal_type1):
    meals_type = {}
    index = 1
    index_2 = 1
    simple_list = []

    for meal in Meals.objects.filter(type=meal_type1):
        if index % 3 != 0:
            simple_list.append(meal)

        else:
            simple_list.append(meal)
            meals_type[index_2] = simple_list
            simple_list = []
            index_2 = index_2 + 1

        index = index + 1

    return meals_type


def index(request):

    return render(request, 'Meals/index.html',
                  {'breakfast': single_meal('sniadanie'),
                   'dinner': single_meal('obiad'),
                   'supper': single_meal('kolacja'),
                   'meala': settings.BASE_DIR}
                  )


def details(request, meal_id):
    return render(request, 'Meals/details.html', {'meals_id': Meals.objects.get(pk = meal_id)})


def new_meal(request):
    form = NewMealsForm(request.POST or None)
    if form.is_valid():
        new_meal = form.save(commit=False)

    return render(request, 'Meals/new_meal.html')