from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.shortcuts import redirect

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
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class CreatePlanDay(CreateView):
    template_name = 'Plan/plans_create_single_plan.html'
    form_class = StartNewDayPlanForm
    queryset = SinglePlan.objects.all()
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


def my_plans(request):
    return render(request, 'Plan/plans_all.html', {'objects': Sprint.objects.all(),
                                                   'new': ['Nowy'],
                                                   'begin': ['Rozpoczety'],
                                                   'products': get_products()})


def details_single_plan(request, plan_id):
    obj = get_object_or_404(SinglePlan, id=plan_id)
    context = {'object': obj}
    return render(request, 'Plan/plans_details_single_plan.html', context=context)


def plan_start_stop(request, plan_id):
    sprint = get_object_or_404(Sprint, id=plan_id)
    if sprint.sprint_status == 'Nowy':
            sprint.sprint_status = 'Rozpoczety'
            sprint.save()
            return redirect(my_plans)

    elif sprint.sprint_status == 'Rozpoczety':
            sprint.sprint_status = 'Skonczony'
            sprint.save()
            return redirect(my_plans)

    return redirect(my_plans)
