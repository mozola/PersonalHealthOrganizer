from django.contrib import admin
from django.urls import path, include

from .views import (index, details, meal_delete_view,
                    MealCreateView, MealUpdateView,
                    ComponentCreateView)


app_name = 'meal'

urlpatterns = [
    path('all/', index, name = 'index'),
    path('new_meal/', MealCreateView.as_view(), name = 'new_meal'),
    path('new_component/', ComponentCreateView.as_view(), name = 'new_component'),
    path('<int:meal_id>/delete/', meal_delete_view, name='delete_meal'),
    # path('<int:meal_id>/detail/', details, name='detail_meal'),
    path('<int:meal_id>/update/', MealUpdateView.as_view(), name='update-view'),
]
