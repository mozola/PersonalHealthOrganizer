# -*- coding: utf-8 -*-
from django.shortcuts import render
from Meals.models import Meals
from .models import SinglePlan


def index(request):
    return render(request, 'MyPlan/index.html')

def new_plan(request):
    return render(request, 'MyPlan/new_plan.html', {'meals': Meals.objects.all()})

def my_plans(request):
    return render(request, 'MyPlan/my_plans.html', {'my_plans': SinglePlan.objects.all()})

def selected(request, meal_id):
    meal = get_object_or_404(Meals, pk=meal_id)

#   try:
#       selected_meals =