# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView

import datetime

from Meal.models import Meal
from .models import SinglePlan, Sprint
from .forms import PlanCreateForm, StartNewDayPlanForm


#  get all products from actual sprint
def get_products():
    components = {}
    for sprint in Sprint.objects.all():
        if sprint.sprint_status == 'Rozpoczety':
            for single in sprint.sprint_parameters.all():
                if single.state != True:
                    for meals in single.meals.all():

                        for a in meals.products.all():
                            if a.component not in components:
                                components[a.component] = [a.count, a.units]
                            else:
                                components[a.component] = [components[a.component][0] + a.count, a.units]
            break
    return components


class CreatePlan(CreateView):
    template_name = 'Plan/plans_create_plan.html'
    form_class = PlanCreateForm
    queryset=get_products()
    success_url='/'

    def form_valid(self, form):
        return super().form_valid(form)


class CreatePlanDay(CreateView):
    template_name='Plan/plans_create_single_plan.html'
    form_class=StartNewDayPlanForm
    queryset = SinglePlan.objects.all()
    success_url='/'

    def form_valid(self, form):
        return super().form_valid(form)


def my_plans(request):
    return render(request, 'Plan/plans_all.html', {'my_plans': Sprint.objects.all(),
                                                    'products': get_products()})


def start_sprint(request):
    components = {}
    state = True
    for sprint in Sprint.objects.all():

        if sprint.sprint_status == 'Nowy':
            for sprint_param in sprint.sprint_parameters.all():
                if sprint_param.plan_date == datetime.date.today():
                    sprint.sprint_status = 'Rozpoczety'
                    sprint.save()
                    return render(request, 'Plan/plans_all.html')

        elif sprint.sprint_status == 'Rozpoczety':

            for sprint_param in sprint.sprint_parameters.all():

                if sprint_param.plan_date ==  datetime.date.today():
                    return render(request, 'Plan/output.html',
                                            {'information': 'Jesteś w aktualnym sprincie',
                                            'plan_object': sprint})


    return render(request, 'Plan/plans_start_plan.html', {'components': components})
