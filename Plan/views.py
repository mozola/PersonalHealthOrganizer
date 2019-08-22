# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import UpdateView
import datetime
from Meal.models import Meal

from .models import SinglePlan
from .models import Sprint

from .forms import StartNewSprintForm


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


def index(request):
    return render(request, 'Plan/index.html')


def new_plan(request):
    return render(request, 'Plan/new_plan.html', {'meals': Meal.objects.all()})


def my_plans(request):
    return render(request, 'Plan/my_plans.html', {'my_plans': Sprint.objects.all(),
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
                    return render(request, 'Plan/output.html',
                                  {'information':
                                   'Jesteś w aktualnym sprincie'})

        else:
            state = False

    if state is False:
        return render(request, 'Plan/output.html',
                                                    {'information':
                                                        'Brak nowego sprintu lub termin nie pasuje do żdnego'})

    return render(request, 'Plan/start_sprint.html', {'components': components})


def update_actual_sprint(request):
    singles = {}
    meals = []
    for sprint in Sprint.objects.all():
        if sprint.sprint_status == 'Rozpoczety':
            for single in sprint.sprint_parameters.all():
                for meal in single.meals.all():
                    # meal.state = True
                    # meal.save()
                    meal_date = single.plan_date
                    meals.append(meal)
                singles[meal_date] = meals
                meals = []
    print(request.POST.getlist('checks'))
    return render(request, 'Plan/update_actual_state.html',
                            {'meals': singles,
                             'products': get_products()})


"""
class PlanUpdateView(UpdateView):
    template_name='Plan/new_plan.html'
    form_class = 
    queryset = Meal.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Meal, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)
"""