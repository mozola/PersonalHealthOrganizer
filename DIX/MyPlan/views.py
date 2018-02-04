# -*- coding: utf-8 -*-

from django.shortcuts import render
import datetime
from Meals.models import Meals
from include import mail
from .models import SinglePlan
from .models import Sprints


def index(request):
    return render(request, 'MyPlan/index.html')


def new_plan(request):
    return render(request, 'MyPlan/new_plan.html', {'meals': Meals.objects.all()})


def my_plans(request):
    return render(request, 'MyPlan/my_plans.html', {'my_plans': Sprints.objects.all()})


def start_sprint(request):
    components = {}
    state = True
    for sprint in Sprints.objects.all():

        if sprint.sprint_status == 'Nowy':

            for sprint_param in sprint.sprint_parameters.all():

                if sprint_param.plan_date == datetime.date.today():

                    sprint.sprint_status = 'Rozpoczety'
                    sprint.save()
                    state = True
                    for single in sprint_param.meals.all():
                        for a in single.components.all():
                            if a.name not in components:
                                components[a.name] = [a.waste, a.units]
                            else:
                                components[a.name] = [components[a.name][0] + a.waste, a.units]
                    break
                else:
                    state = False
        elif sprint.sprint_status == 'Rozpoczety':

            for sprint_param in sprint.sprint_parameters.all():
                if sprint_param.plan_date ==  datetime.date.today():
                    state = True
                    return render(request, 'MyPlan/output.html',
                                  {'information':
                                       'Jesteś w aktualnym sprincie'})

        else:
            state = False

    if state is False:
        return render(request, 'MyPlan/output.html',
                                                    {'information':
                                                        'Brak nowego sprintu lub termin nie pasuje do żdnego'})

    mail.send_main(components)
    return render(request, 'MyPlan/start_sprint.html', {'components': components})


def update_actual_sprint(request):
    meals = {}
    for sprint in Sprints.objects.all():
        if sprint.sprint_status == 'Rozpoczety':
            for single in sprint.sprint_parameters.all():
                for meal in single.meals.all():
                    meal.state = True
                    meal.save()
                    meals[meal.name] = meal.state
    return render(request, 'MyPlan/update_actual_state.html', {'meals': meals})