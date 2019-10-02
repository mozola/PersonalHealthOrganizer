from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView

from .models import Meal, Component
from .forms import NewMealForm, NewComponent


def single_meal(meal_type1):
    for meal in Meal.objects.filter(types=meal_type1):
        yield meal


def index(request):
    breakfast = list(single_meal('sniadanie'))
    dinner = list(single_meal('obiad'))
    supper = list(single_meal('kolacja'))

    return render(request, 'Meal/meal_main.html',
                  {'breakfast': breakfast,
                   'dinner': dinner,
                   'supper': supper})


def details(request, meal_id):
    obj = get_object_or_404(Meal, id=meal_id)
    context = {'object': obj}

    return render(request, 'Meal/meal_detail.html', context=context)


def meal_delete_view(request, meal_id):
    obj = get_object_or_404(Meal, id=meal_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    return render(request, 'Meal/meal_delate.html')


class MealDetailView(DetailView):
    template_name = ''
    queryset = Meal.objects.all()


class ComponentCreateView(CreateView):
    template_name = 'Meal/meal_component_new.html'
    form_class = NewComponent
    queryset = Component.objects.all()
    success_url = '/meal/new_component'

    def form_valid(self, form):
        return super().form_valid(form)


class MealCreateView(CreateView):
    template_name = 'Meal/meal_new.html'
    form_class = NewMealForm
    queryset = Meal.objects.all()
    success_url = '/meal/new_meal'

    def form_valid(self, form):
        return super().form_valid(form)


class MealUpdateView(UpdateView):
    template_name = 'Meal/meal_new.html'
    form_class = NewMealForm

    def get_object(self):
        meal_id = self.kwargs.get("meal_id")
        return get_object_or_404(Meal, id=meal_id)

    def form_valid(self, form):
        return super().form_valid(form)
