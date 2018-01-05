# -*- coding: utf-8 -*-
from django.shortcuts import render
from Meals.models import Meals


def index(request):
    return render(request, 'MyPlan/index.html')

def new_plan(request):
    return render(request, 'MyPlan/new_plan.html', {'meals': Meals.objects.all()})